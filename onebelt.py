from fitting import *
from functions import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
from astropy.table import Table

def onebelts(i):
    
    filein = Table.read('%s' % (i), format='ipac')
    DataWave = filein['wavelength']
    DataFlux = filein['flux']
    DataUncert = filein['error']
    Source = tname(i)
    Tstar = tstar(i)
    NextGen = ngfind(i)
    NGwave, NGflux = data_ng('nextgen/%s' % (NextGen))
    
    print 'Running onebelt with star %s.' % (Source)

    
    #Variables
    wave = np.arange(1e-6, 500e-6, 1e-6)                                       #wave range in meters
    wavew = np.arange(1, 500, 1)                                               #wave range in microns
    NGfluxDataWave = np.interp(DataWave,NGwave,NGflux)                                                          #interpolation of NextGen in data wave range
    Yw = np.interp(wavew,NGwave,NGflux)                                        #interpolation of NextGen data in BlackBody wave range
    T1 = 100                                                                   #initlal temperature for inner belt
    T2 = 100                                                                   #initial temperature for outer belt
    num = 1
    
    #normalizer functions
    Yn = norm_ng(DataWave,DataFlux,NGwave,NGflux)                              #initial normalizer for NextGen values
    norm = normilize(DataWave,DataFlux)                                        #initial normalizers for blackdodies
    
    #this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
    def forwardmodel(DataWave, T1, N1, Ns):                                    #function used by curve_fit
        from functions import bbl
        return N1*bbl(DataWave,T1) + Ns*NGfluxDataWave
    
    try:    
        popt, pcov = curve_fit(forwardmodel, DataWave, DataFlux, p0=(100,norm,Yn), sigma=DataUncert) #find values for the fitting 
        uncert = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value
    except:
        popt = [100, norm, Yn]
        uncert = [1]
        print 'could not complete fitting'
        Source = Source + 'with unfit parameters and'
    
    NGflux *= popt[2]                                                                   #normalizes the NextGen values
    
    #Main SED info
    inner = planck(wave, popt[0]) * popt[1]                                        #calls function for inner blackbody
    some = Yw*popt[2] + planck(wave, popt[0]) * popt[1]                                                  #creates the summation value array 
    
    #Excess info
    excess = DataFlux - NGfluxDataWave*popt[2]
    #inner see above
    #outer see above
    exsum = inner 
    
    #Residual info
    Yr = np.interp(DataWave, wavew, some)
    res = (DataFlux - Yr) / DataUncert
    zero = wavew * 0
    
    #Chi Calculator
    DoF = len(DataWave)-3
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
    plt.subplot(311)                                                               #first subplot main SED
    plt.ioff()    
    plt.title('%s with reduced chi square of %3f' % (Source, rechisq))                                                        #title of plot
    plt.loglog(NGwave,NGflux, 'grey', label='NextGen')                                         #NextGen plot
    plt.plot(DataWave,DataFlux, 'k.', label='IR Data')                                           #plots spectral data
    plt.errorbar(DataWave,DataFlux,yerr=DataUncert,linestyle="none")
    plt.plot(wavew,some, 'y--', label='Best Fit')                                  #plots the summation
    plt.plot(wavew,inner, 'r-', label='T=%3i$\pm$%1i' % (popt[0],uncert[0]))       #plots the inner belt
    plt.ylabel(r'F$_\nu$ (Jy)')
    plt.legend(frameon=True)                                                       #creates legend
    plt.xlim(0.2*min(DataWave),1.5*max(DataWave))                                                                #locks x limits for plot
    plt.ylim(1e-2*ylim,100*max(DataFlux)) 
    
    #EXCESS PLOT
    plt.subplot(312)          #second subplot of EXCESS
    plt.ioff()    
    plt.plot(wavew,exsum, 'y--', label='Best Fit')                                  #plots the summation
    plt.loglog(DataWave,excess, 'k.', label='Excess')
    plt.plot(wavew,inner, 'r-', label='T=%3i$\pm$%1i' % (popt[0],uncert[0]))       #plots the inner belt
    plt.plot(wavew,exsum, 'y--', label='Best Fit')                                  #plots the summation
    plt.ylabel(r'F$_\nu$ (Jy)')
    plt.legend(frameon=True)                                                       #creates legend
    plt.xlim(0.7*min(DataWave),1.5*max(DataWave))                                                                #locks x limits for plot
    plt.ylim(1e-2*min(excess),100*max(excess)) 
    
    #RESIDUAL PLOT
    plt.subplot(313)
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
        plt.savefig('Results/%s with %i belts' % (Source, num))
    except:
        print 'Could not store plot'
    plt.close
    
    Values = [Source, Tstar, popt[0], popt[1], popt[2], rechisq]
    
    return Values
