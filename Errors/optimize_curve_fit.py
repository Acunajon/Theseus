import math
import numpy as np
from scipy.optimize import curve_fit

"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)
k = 1.38064852*10**(-23)
c = 299792458   
"""CONSTANTS"""


#For testing sample1: change the open() to the directory of your file. 


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


def Planck_3(Wav, T, Norm, T_Inner, Norm_Inner, T_Outer, Norm_Outer):
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
    return Flux_3
    
    
def Planck_1(Wav, T, Norm):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    return Flux

    
popt_trf1, pcov_trf1 = curve_fit(Planck_1, x, y, sigma=z, method='trf')
print popt_trf1
print pcov_trf1

popt_dogbox1, pcov_dogbox1 = curve_fit(Planck_1, x, y, sigma=z, method='dogbox')
print popt_dogbox1
print pcov_dogbox1
    
popt_MAIN1, pcov_MAIN1 = curve_fit(Planck_1, x, y, sigma=z)
print popt_MAIN1
print pcov_MAIN1

popt_trf3, pcov_trf3 = curve_fit(Planck_3, x, y, sigma=z, method='trf')
print popt_trf3
print pcov_trf3

popt_dogbox3, pcov_dogbox3 = curve_fit(Planck_3, x, y, sigma=z, method='dogbox')
print popt_dogbox3
print pcov_dogbox3
    
popt_MAIN3, pcov_MAIN3 = curve_fit(Planck_3, x, y, sigma=z)
print popt_MAIN3
print pcov_MAIN3



"""

C:\Program Files\Anaconda2\lib\site-packages\scipy\optimize\minpack.py:715:
OptimizeWarning: Covariance of the parameters could not be estimated
category=OptimizeWarning)


OptimizeWarning

    if covariance of the parameters can not be estimated.


"""