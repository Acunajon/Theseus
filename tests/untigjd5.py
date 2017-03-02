"""
JonathanAcuna
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit, minimize



"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)
k = 1.38064852*10**(-23)
c = 299792458   
"""CONSTANTS"""


"""OPENS THE DESIRED DATA FILE"""
sample1 = open('C:\Users\jma48203\Desktop\Thesis\Initial data\DDisk_17jun13_allIRflux.txt' , 'r')
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




"""Variables"""   """THIS WILL BE FITTED"""
T = 10000
T_Hot = 235
T_Cold = 80

Norm = 5.96208351173e+26
Norm_Cold = Norm*20000
Norm_Hot = Norm*60
"""END OF BASE VARIABLES"""    

wave = np.arange(1e-6, 500e-6, 1e-6)

planck = lambda A, B, norm, Wav: (A/Wav**5)*(1/(e**(B)-1))*Conv*norm

def Planck_3(Wav, T, Norm, T_Inner, Norm_Inner, T_Outer, Norm_Outer):
    print Wav
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_Inner)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Inner = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_Inner
    b_OUT = h*c/(Wav*k*T_Outer)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Outer = (a/Wav**5)*(1/(e**(b_OUT)-1))*Conv*Norm_Outer
    Flux_3 = Flux + Flux_Inner + Flux_Outer
    return Flux_3, Flux, Flux_Inner, Flux_Outer 
    
    
def Re_Chi_2(Dat, Theo, Uncert, DoF=2, Para=1):
    Chi = 0
    for i in range(len(Dat)):
        Chi += ((Dat[i] - Theo[i])**2)/(Uncert[i]**2)
    return Chi/(DoF - Para)
    
Flux_S = []
Flux_in = []
Flux_out = []
Flux_all =[]
"""for i in wave:
    Flux_3, Flux, Flux_IN, Flux_OUT = Planck_3(i, T, Norm, T_Hot, Norm_Hot, T_Cold, Norm_Cold)
    Flux_S.append(Flux)
    Flux_in.append(Flux_IN)
    Flux_out.append(Flux_OUT)
    Flux_all.append(Flux_3)
"""
    
Po = [T,T_Hot,T_Cold,Norm,Norm_Cold,Norm_Hot]
x = np.array([0,1,5])
print x.shape
x = np.reshape(x, (len(x),1))
print x.shape
y = np.array([1, 2,6])
popt, pcov = curve_fit(Planck_3, x, y, p0=np.array(Po))
print popt
print pcov
    
plt.loglog(x,y, 'k.')
plt.loglog(wave*1e6, Flux_S, 'y-') 
plt.loglog(wave*1e6, Flux_in, 'r-') 
plt.loglog(wave*1e6, Flux_out, 'b-') 
plt.loglog(wave*1e6, Flux_all, 'g--', label='Curve Sum') 
plt.errorbar(x,y,yerr=z,linestyle="none")
plt.show()