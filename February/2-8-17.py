"""
JonathanAcuna
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit



"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)
k = 1.38064852*10**(-23)
c = 299792458   
"""CONSTANTS"""


"""OPENS THE DESIRED DATA FILE"""
sample1 = open('C:\Users\jma48203\Desktop\Thesis\Initial data\DDisk_17jun13_allExcess.txt' , 'r')
s1=sample1.readlines()
s1 = np.array(map(lambda x: x.strip(), s1))
d = np.array(map(lambda x: x.split(), s1)).reshape((-1,3))
d = np.delete(d, [0,1,2]).reshape((-1,3))
d = d.astype(float)

x = []
y = []
z = []

for i in d:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])
"""DESIRED DATA FILE"""


def Planck_2(Wav, T, Norm, T_IN, Norm_IN):
    'Function start'
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_IN)
    Conv = ((Wav**2)/c)*10**-19
    Flux_IN = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_IN
    Flux_2 = Flux + Flux_IN
    return Flux_2, Flux, Flux_IN
    

"""Variables"""   """THIS WILL BE FITTED"""
T = 10000
T_Hot = 235
T_Cold = 80

Norm = 5.96208351173e+26
Norm_Cold = Norm*20000
Norm_Hot = Norm*60
"""END OF BASE VARIABLES"""    
    
wave = np.arange(1e-6, 500e-6, 1e-6)
 





Flux = []
Flux_IN = []
Flux_2 =[]
for i in wave:
    #X_Sum.append(Planck_2(i,T_Hot,Norm_Hot,T_Cold,Norm_Cold))
    flux_2, flux, flux_IN = Planck_2(i,T_Hot,Norm_Hot,T_Cold,Norm_Cold)
    Flux.append(flux)
    Flux_IN.append(flux_IN)
    Flux_2.append(flux_2)

Theo = []
for i in x:
    Theo.append(Planck_2(i*1e-6,T_Hot,Norm_Hot,T_Cold,Norm_Cold)[0])


    
   
    
Theory = np.array(Theo)
Obs = np.array(x)
uncert = np.array(z)


Chi = sum(((Obs - Theory)**2)/(uncert**2))
Re_Chi = Chi/(len(x)-4)
    

print 4546
    
popt, pcov = curve_fit(Planck_2, np.array(x), np.array(y), sigma=np.array(z))
print popt
print pcov
    
print 5657
    

plt.loglog(x,y, 'k.')
plt.loglog(wave*1e6, Flux, 'r-') 
plt.loglog(wave*1e6, Flux_IN, 'b-') 
plt.loglog(wave*1e6, Flux_2, 'g--', label='Curve Sum') 
plt.errorbar(x,y,yerr=z,linestyle="none")
plt.show()