"""
Plank's Law
@author: jma48203
"""

import math
#import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#constants
pi = math.pi
e = math.e
#h = sp.hbar
h = 6.62607004*10**(-34)          #m**2*kg/s
#k = sp.Stefan_Boltzman
k = 1.38064852*10**(-23)          #m**2*kg/(s**2*K)
#c = sp.c
c = 299792458                     #m/s


Wv = 10.0560000
Flx = 0.152130000


#data from first array.

#Determining initial temperature value
X = (4*h*pi*c**(2))/Flx*Wv**(5)
B = np.log(X)
T = (h*c)/(Wv*k*B+1)
T = T.astype(float)

print T
#Main function
def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Flux = (a/Wav**5)*(1/(e**(b)+1))
    return Flux
    
    
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 
FluxT = plank(wavelengths, T)

#This plots are reerence for multiple temperatures
Flux1000 = plank(wavelengths, 1000)
Flux2000 = plank(wavelengths, 2000)
Flux3000 = plank(wavelengths, 3000)
Flux4000 = plank(wavelengths, 4000)
Flux5000 = plank(wavelengths, 5000)
Flux6000 = plank(wavelengths, 6000)



plt.hold(True)
plt.plot(wavelengths*1e9, FluxT, 'r-') 

#Multiple temperatures
plt.plot(wavelengths*1e9, Flux1000, 'b-') 
plt.plot(wavelengths*1e9, Flux2000, 'g-') 
plt.plot(wavelengths*1e9, Flux3000, 'g-') 
plt.plot(wavelengths*1e9, Flux4000, 'g-') 
plt.plot(wavelengths*1e9, Flux5000, 'g-') 
plt.plot(wavelengths*1e9, Flux6000, 'g-') 



"""NOTES
np.log is ln, whereas np.log10 is your standard base 10 log.



"""
