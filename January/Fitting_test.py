"""
JonathanAcuna
"""



import math
import numpy as np
import matplotlib.pyplot as plt


"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)          #m**2*kg/s
k = 1.38064852*10**(-23)          #m**2*kg/(s**2*K)
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

for i in d:
    x.append(i[0])
    y.append(i[1])
"""DESIRED DATA FILE"""


"""PLANK FUNCTION"""
def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)+1))*Conv
    return Flux
"""PLANK FUNCTION END"""


"""WAVE LENGTH RANGE"""
wave = np.arange(1e-9, 500e-6, 1e-7) 
"""WAVE LENGTH RANGE"""








"""THIS IS THE BEGINNING FOR THE STAR PLOT"""
T = 10000
Flux = plank(wave, T)
Xave=sum(x[0:6])/5
Fave=sum(Flux[0:6])/5
Norm = Xave/Fave
FluxN = Flux*Norm
"""END OF STAR DATA FOR STAR PLOT"""



"""FITTING FOR PARAMETERS"""
dub = []
dub.append(x[0:10])
print dub
for i in dub:
    break

"""END OF FITTING"""



"""THIS IS THE BEGINNING OF ALL THE PLOT OVERLAYS"""
plt.hold(True)
plt.loglog(wave*1e6, FluxN, 'y-') 
plt.loglog(x,y,'k.')
"""END OF PLOT LINES"""


"""AXIS AND LABELS"""
plt.show()
plt.ylabel('Flux (Jy)')
plt.xlabel('Wavelength (microns)')
"""END OF ALL PLOT LINES"""

"""PLOT LIMITS"""
#plt.xlim([0.1,520])
#plt.ylim([0.0000001,100])
"""PLOT LIMITS"""



"""
np.log is ln, whereas np.log10 is your standard base 10 log.
plt.loglog   plots with axis in log vs log.
"""