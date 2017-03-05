"""FITTING"""

"""
JonathanAcuna
"""

import math
import numpy as np
import matplotlib.pyplot as plt




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

def Planck_3(Wav, T, Norm, T_Inner, Norm_Inner, T_Outer, Norm_Outer):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux_S = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_Inner)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Inner = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_Inner
    b_OUT = h*c/(Wav*k*T_Outer)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Outer = (a/Wav**5)*(1/(e**(b_OUT)-1))*Conv*Norm_Outer
    Flux_3 = Flux_S + Flux_Inner + Flux_Outer
    return Flux_3, Flux_S, Flux_Inner, Flux_Outer
    
    
def Planck_3_X(Wav, T, Norm, T_Inner, Norm_Inner, T_Outer, Norm_Outer):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux_S = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_Inner)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Inner = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_Inner
    b_OUT = h*c/(Wav*k*T_Outer)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Outer = (a/Wav**5)*(1/(e**(b_OUT)-1))*Conv*Norm_Outer
    Flux_X = Flux_S + Flux_Inner + Flux_Outer
    return Flux_X
    
    
def Re_Chi_2(Dat, Theo, Uncert, DoF=2, Para=1):
    Chi = 0
    for i in range(len(Dat)):
        Chi += ((Dat[i] - Theo[i])**2)/(Uncert[i]**2)
    return Chi/(DoF - Para)
    
#Chi = Re_Chi_2(y,)

Flux_all, Flux_S, Flux_in, Flux_out = Planck_3(wave, T, Norm, T_Hot, Norm_Hot, T_Cold, Norm_Cold)

Flux_all_X = []

for i in x:
    TOLS = Planck_3_X(i, T, Norm, T_Hot, Norm_Hot, T_Cold, Norm_Cold)
    Flux_all_X.append(TOLS)

plt.loglog(x,y, 'k.')
plt.loglog(x,Flux_all_X, 'r.')
plt.loglog(wave*1e6, Flux_S, 'y-') 
plt.loglog(wave*1e6, Flux_in, 'r-') 
plt.loglog(wave*1e6, Flux_out, 'b-') 
plt.loglog(wave*1e6, Flux_all, 'g--', label='Curve Sum') 
plt.errorbar(x,y,yerr=z,linestyle="none")
plt.show()