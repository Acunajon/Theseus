from fitting import *
from functions import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
from astropy.table import Table

def nobelts(i):
    
    filein = Table.read('%s' % (i), format='ipac')
    DataWave = filein['wavelength']
    DataFlux = filein['flux']
    DataUncert = filein['error']
    Source = tname(i)
    try:
        Tstar = tstar(i)
    except:
        Tstar = 0
        print '%s has no temperature' % (Source)
    NextGen = ngfind(i)
    NGwave, NGflux = data_ng('nextgen/%s' % (NextGen))
    
    print 'Running nobelt with star %s.' % (Source)

    
    #Variables
    wave = np.arange(1e-6, 500e-6, 1e-6)                                           #wave range in meters
    wavew = np.arange(1, 500, 1)                                                   #wave range in microns
    NGfluxDataWave = np.interp(DataWave,NGwave,NGflux)                                                          #interpolation of NextGen in data wave range
    Yw = np.interp(wavew,NGwave,NGflux)                                                      #interpolation of NextGen data in BlackBody wave range
    T1 = 100                                                                       #initlal temperature for inner belt
    T2 = 100                                                                       #initial temperature for outer belt
    num = 0
    
    #normalizer functions
    Yn = norm_ng(DataWave,DataFlux,NGwave,NGflux)                                                          #initial normalizer for NextGen values
    norm = normilize(DataWave,DataFlux)                                                               #initial normalizers for blackdodies
    
    #this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
    def forwardmodel(DataWave, Ns):                                       #function used by curve_fit
        from functions import bbl
        return Ns*NGfluxDataWave
    try:    
        popt, pcov = curve_fit(forwardmodel, DataWave, DataFlux, p0=(Yn), sigma=DataUncert) #find values for the fitting 
        uncert = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value
    except:
        popt = [Yn]
        print 'could not complete fitting'
        Source = Source + 'with unfit parameters and'

    
    NGflux *= popt[0]                                                                   #normalizes the NextGen values
    
    #Main SED info
                                                                              #calls function for inner blackbody
    some = Yw*popt[0]                                                      #creates the summation value array 
    
    #Excess info
    excess = DataFlux - NGfluxDataWave*popt[0]
    #inner see above
    #outer see above
    
    #Residual info
    Yr = np.interp(DataWave, wavew, some)
    res = (DataFlux - Yr) / DataUncert
    zero = wavew * 0
    
    #Chi Calculator
    DoF = len(DataWave)-1
    chi = (DataFlux - Yr)/DataUncert
    chisq = np.dot(chi, chi)
    rechisq = chisq / DoF
    
    ylim = min(DataFlux)
    if ylim < 0:
        ylim *= -1
    
    plt.figure() 
    plt.ioff()    
    plt.xlabel(r'$\lambda$ ($\mu$m)')                                              #sets x label for plot
    plt.ylabel(r'F$_\nu$ (Jy)')                                                    #sets y label for plot
    #plt.grid(False)
    #plt.xlim(.1,300)                                                              #locks x limits for plot
    #plt.ylim(6.0e-3,20)                                                           #locks y limits for plot
    #plt.xlim(3,300)                                                                #locks x limits for plot
    #plt.ylim(6.0e-3,1) 
    
    #SED PLOT
    plt.subplot(211)                                                               #first subplot main SED
    plt.ioff()    
    plt.title('%s with reduced chi square of %3f' % (Source, rechisq))                                                        #title of plot
    plt.loglog(NGwave,NGflux, 'grey', label='NextGen')                                         #NextGen plot
    plt.plot(DataWave,DataFlux, 'k.', label='IR Data')                                           #plots spectral data
    plt.errorbar(DataWave,DataFlux,yerr=DataUncert,linestyle="none")
    plt.plot(wavew,some, 'y--', label='Best Fit')                                  #plots the summation
    plt.ylabel(r'F$_\nu$ (Jy)')
    plt.legend(frameon=True)                                                       #creates legend
    plt.xlim(0.2*min(DataWave),1.5*max(DataWave))                                                                #locks x limits for plot
    plt.ylim(1e-2*ylim,100*max(DataFlux)) 
    
    #RESIDUAL PLOT
    plt.subplot(212)
    plt.ioff()    
    plt.loglog(DataWave, res,'k.',linewidth=0.1, label='Residual') 
    plt.plot(wavew, zero, 'k--')
    plt.ylabel(r'Residual/$\sigma$')
    plt.xlabel(r'$\lambda$ ($\mu$m)')
    plt.yscale('linear')
    plt.legend(frameon=True)                                                       #creates legend
    plt.xlim(3,300)                                                                #locks x limits for plot
    #plt.ylim(-2,2) 
    
    plt.subplots_adjust(hspace=0)
    plt.ioff()    
    try:
        plt.savefig('Results/%s with %i belts.' % (Source, num))
    except:
        print 'Could not store plot.'
    plt.close
    
    Values = [Source, Tstar, popt[0], rechisq]
    
    return Values
