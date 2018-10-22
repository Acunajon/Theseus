from fitting import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

"""
NOTE TO FUTURE VIEWER:
this is a template fufilling the simplest BlackBody fitting routine requirements. 
"""


"""
x = DataWave
y = DataFlux
z = DataUncert
X = NGwave
Y = NGflux
T = Tstar
Ys = NGfluxDataWave
"""

DataWave,DataFlux,DataUncert = data('batch_list/DDisk_17jun13_allIRflux.txt')                         #opens data file
NGwave, NGflux = data_ng('nextgen/xp00_8800g40.txt')                                     #opens NextGen file
Tstar = 8870                                                                       #star temperature
Source = 'SourceName'        
    
#Variables
wave = np.arange(1e-6, 500e-6, 1e-6)                                           #wave range in meters
wavew = np.arange(1, 500, 1)                                                   #wave range in microns
NGfluxDataWave = np.interp(DataWave,NGwave,NGflux)                                                          #interpolation of NextGen in data wave range
Yw = np.interp(wavew,NGwave,NGflux)                                                      #interpolation of NextGen data in BlackBody wave range
T1 = 100                                                                       #initlal temperature for inner belt
T2 = 100                                                                       #initial temperature for outer belt

#normalizer functions
Yn = norm_ng(DataWave,DataFlux,NGwave,NGflux)                                                          #initial normalizer for NextGen values
norm = normilize(DataWave,DataFlux)                                                               #initial normalizers for blackdodies

#this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
def forwardmodel(DataWave, T1, T2, N1, N2, Ns):                                       #function used by curve_fit
    from functions import bbl
    return N1*bbl(DataWave,T1) + N2*bbl(DataWave,T2) + Ns*NGfluxDataWave
    
popt, pcov = curve_fit(forwardmodel, DataWave, DataFlux, p0=(100,100,norm,norm,Yn), sigma=DataUncert) #find values for the fitting 
uncert = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value

NGflux *= popt[4]                                                                   #normalizes the NextGen values

#Main SED info
inner = planck(wave, popt[0]) * popt[2]                                        #calls function for inner blackbody
outer = planck(wave, popt[1]) * popt[3]                                        #calls function for outer blackbody
some = Yw*popt[4] + planck(wave,popt[0],popt[2]) + planck(wave,popt[1],popt[3])#creates the summation value array 

#Excess info
excess = DataFlux - NGfluxDataWave*popt[4]
#inner see above
#outer see above
exsum = inner + outer

#Residual info
Yr = np.interp(DataWave, wavew, some)
res = (DataFlux - Yr) / DataUncert
zero = wavew * 0

#Chi Calculator
DoF = len(DataWave)-5
chi = (DataFlux - Yr)/DataUncert
chisq = np.dot(chi, chi)
rechisq = chisq / DoF


plt.figure()     
plt.xlabel(r'$\lambda$ ($\mu$m)')                                              #sets x label for plot
plt.ylabel(r'F$_\nu$ (Jy)')                                                    #sets y label for plot
#plt.grid(False)
#plt.xlim(.1,300)                                                              #locks x limits for plot
#plt.ylim(6.0e-3,20)                                                           #locks y limits for plot
plt.xlim(3,300)                                                                #locks x limits for plot
plt.ylim(6.0e-3,1) 

#SED PLOT
plt.subplot(311)                                                               #first subplot main SED
plt.title('%s with reduced chi square of %3f' % (Source, rechisq))                                                        #title of plot
plt.loglog(NGwave,NGflux, 'c:', label='NextGen')                                         #NextGen plot
plt.plot(DataWave,DataFlux, 'k.', label='IR Data')                                           #plots spectral data
plt.errorbar(DataWave,DataFlux,yerr=DataUncert,linestyle="none")
plt.plot(wavew,some, 'y--', label='Best Fit')                                  #plots the summation
plt.plot(wavew,inner, 'b-', label='T=%3i$\pm$%1i' % (popt[0],uncert[0]))       #plots the inner belt
plt.plot(wavew,outer, 'r-', label='T=%3i$\pm$%1i' % (popt[1],uncert[1]))       #plots the outer belt
plt.ylabel(r'F$_\nu$ (Jy)')
plt.legend(frameon=True)                                                       #creates legend
plt.xlim(3,300)                                                                #locks x limits for plot
plt.ylim(2.0e-3,1) 

#EXCESS PLOT
plt.subplot(312)          #second subplot of EXCESS
plt.loglog(DataWave,excess, 'k.', label='Excess')
plt.plot(wavew,inner, 'b-', label='T=%3i$\pm$%1i' % (popt[0],uncert[0]))       #plots the inner belt
plt.plot(wavew,outer, 'r-', label='T=%3i$\pm$%1i' % (popt[1],uncert[1]))       #plots the outer belt
plt.plot(wavew,exsum, 'y--', label='Best Fit')                                  #plots the summation
plt.ylabel(r'F$_\nu$ (Jy)')
plt.legend(frameon=True)                                                       #creates legend
plt.xlim(3,300)                                                                #locks x limits for plot
plt.ylim(2.0e-3,1) 

#RESIDUAL PLOT
plt.subplot(313)
plt.loglog(DataWave, res,'k.',linewidth=0.1, label='Residual') 
plt.plot(wavew, zero, 'k--')
plt.ylabel(r'Residual over Uncertainty')
plt.xlabel(r'$\lambda$ ($\mu$m)')
plt.yscale('linear')
plt.legend(frameon=True)                                                       #creates legend
plt.xlim(3,300)                                                                #locks x limits for plot
#plt.ylim(-2,2) 

plt.subplots_adjust(hspace=0)
plt.savefig('%s' % (Source))












