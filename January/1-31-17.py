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


"""PLANK FUNCTION"""
def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv
    return Flux
"""PLANK FUNCTION END"""


"""WAVE LENGTH RANGE"""
wave = np.arange(1e-9, 500e-6, 1e-6) 
"""WAVE LENGTH RANGE"""






"""THIS IS THE BEGINNING FOR THE STAR PLOT"""
T = 10000
Flux = plank(wave, T)
Xave=sum(x[0:5])/5
Fave=sum(Flux[0:5])/5
Norm = Xave/Fave
FluxN = Flux*Norm
"""END OF STAR DATA FOR STAR PLOT"""


"""TEMPERATURE PARAMETERS"""
T_Hot = 235
T_Cold = 60
"""TEMPERATURES"""


"""NORMALIZERS"""
Norm_Cold = Norm*2000
Norm_Hot = Norm*10
"""END OF PARAMETERS"""


"""FITTING FOR PARAMETERS"""

"""END OF FITTING"""


"""START OF DATA FOR HOT DATA CURVE"""
Flux_Hot = plank(wave, T_Hot)
Flux_Hot_N = Flux_Hot*Norm_Hot
"""END OF HOT CURVE DATA PLOT INFO"""


"""COLD DATA START PLOT INFO"""
Flux_Cold = plank(wave, T_Cold)
Flux_Cold_N = Flux_Cold*Norm_Cold
"""COLD DATA END PLOT INFO"""


"""START OF SUM PLOT CURVE"""
X_sum = []
for i in wave:
    a_sum = plank(i, T)
    b_sum = plank(i, T_Hot)
    c_sum = plank(i, T_Cold)
    X_sum.append(a_sum*Norm + b_sum*Norm_Hot + c_sum*Norm_Cold)
"""END OF SUM PLOT CURVE"""


"""Chi^2 ROUTINE"""
Theo = []
for i in x:
    a_sum = plank(i, T)
    b_sum = plank(i, T_Hot)
    c_sum = plank(i, T_Cold)
    Theo.append(a_sum*Norm + b_sum*Norm_Hot + c_sum*Norm_Cold)

Theory = np.array(Theo)
Obs = np.array(x)
uncert = np.array(z)


Chi = sum(((Obs - Theory)**2)/(uncert**2))
Re_Chi = Chi/(len(x)-4)
print 'Chi', Chi
print 'Re_Chi', Re_Chi
"""Chi^2 ROUTINE"""


"""FITTING-------THIS MUST MINIMIZE THE CHI VALUE"""
"""------------WILL BE ADDED ONCE FINISHED-------"""
"""FITTING-------THIS MUST MINIMIZE THE CHI VALUE"""


"""THIS IS THE BEGINNING OF ALL THE PLOT OVERLAYS"""
plt.hold(True)
plt.loglog(wave*1e6, FluxN, 'y-') 
plt.loglog(wave*1e6, Flux_Hot_N, 'r-') 
plt.loglog(wave*1e6, Flux_Cold_N, 'b-') 
plt.loglog(wave*1e6, X_sum, 'g--') 
plt.loglog(x,y, 'k.')
plt.errorbar(x,y,yerr=z,linestyle="none")
"""END OF PLOT LINES"""


"""AXIS AND LABELS"""
plt.ylabel('Flux (Jy)')
plt.xlabel('Wavelength (microns)')
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