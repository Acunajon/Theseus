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



def Planck_1(Wav, T, Norm):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    return Flux

def Planck_2(Wav, T, Norm, T_IN, Norm_IN):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_IN)
    Conv = ((Wav**2)/c)*10**-19
    Flux_IN = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_IN
    Flux_T = Flux + Flux_IN
    return Flux_T
    
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
    Flux_T = Flux + Flux_Inner + Flux_Outer
    return Flux_T



"""Variables"""   """THIS WILL BE FITTED"""
T = 10000
T_Hot = 235
T_Cold = 80

Norm = 5.96208351173e+26
Norm_Cold = Norm*20000
Norm_Hot = Norm*60
"""END OF BASE VARIABLES"""


"""WAVE LENGTH RANGE"""
wave = np.arange(1e-6, 500e-6, 1e-6)
"""WAVE LENGTH RANGE"""



"""START OF DATA FOR HOT DATA CURVE"""
Flux = Planck_1(wave, T, Norm)
Flux_Hot = Planck_1(wave, T_Hot, Norm_Hot)
Flux_Cold = Planck_1(wave, T_Cold, Norm_Cold)
"""COLD DATA END PLOT INFO"""



X_Sum = []
for i in wave:
    X_Sum.append(Planck_3(i,T,Norm,T_Hot,Norm_Hot,T_Cold,Norm_Cold))
    
Theo = []
for i in x:
    Theo.append(Planck_3(i*1e-6,T,Norm,T_Hot,Norm_Hot,T_Cold,Norm_Cold))
    

Theory = np.array(Theo)
Obs = np.array(x)
uncert = np.array(z)


Chi = sum(((Obs - Theory)**2)/(uncert**2))
Re_Chi = Chi/(len(x)-4)
print 'Chi', Chi
print 'Re_Chi', Re_Chi
"""Chi^2 ROUTINE"""


"""FITTING-------THIS MUST MINIMIZE THE CHI VALUE"""
print 'Norm',        Norm
print 'T_Hot',       T_Hot
print 'Norm_Hot',    Norm_Hot
print 'T_Cold',      T_Cold
print 'Norm_Cold',   Norm_Cold


#while Re_Chi > 5:
#    pass
"""FITTING-------THIS MUST MINIMIZE THE CHI VALUE"""


"""THIS IS THE BEGINNING OF ALL THE PLOT OVERLAYS"""
plt.hold(True)
plt.loglog(wave*1e6, Flux, 'y-') 
plt.loglog(wave*1e6, Flux_Hot, 'r-') 
plt.loglog(wave*1e6, Flux_Cold, 'b-') 
plt.loglog(x, Theo, 'ro', label='Theory') 
plt.loglog(wave*1e6, X_Sum, 'g--', label='Curve Sum') 
plt.loglog(x,y, 'k.')
plt.errorbar(x,y,yerr=z,linestyle="none")
"""END OF PLOT LINES"""


"""AXIS AND LABELS"""
plt.title(Re_Chi)
plt.ylabel('Flux (Jy)')
plt.xlabel('Wavelength (microns)')
"""
txt = '''
Norm       %d
T_Hot      %d
Norm_Hot   %d
T_Cold     %d
Norm_Cold  %d
Re_Chi     %d
''' % (Norm, T_Hot, Norm_Hot, T_Cold, Norm_Cold, Re_Chi)

plt.text(.15,.1,txt)
"""

"""END OF ALL PLOT LINES"""

"""PLOT LIMITS"""
plt.xlim([0.1,520])
plt.ylim([0.0000001,100])
"""PLOT LIMITS"""

plt.show()

"""
np.log is ln, whereas np.log10 is your standard base 10 log.
plt.loglog   plots with axis in log vs log.
"""