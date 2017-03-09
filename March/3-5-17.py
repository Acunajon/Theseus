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
def plank(Wav, T=100, Norm=1):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    return Flux
"""PLANK FUNCTION END"""
"""WAVE LENGTH RANGE"""
wave = np.arange(1e-6, 500e-6, 1e-6) 
"""WAVE LENGTH RANGE"""
"""THIS IS THE BEGINNING FOR THE STAR PLOT"""
T = 10000
Flux = plank(wave, T, 1)
"""END OF STAR DATA FOR STAR PLOT"""
"""TEMPERATURE PARAMETERS"""
T_Hot = 235
T_Cold = 80
"""TEMPERATURES"""
"""NORMALIZERS"""
Xave=(sum(x[0:5]))/5
Fave=(sum(Flux[0:5]))/5
Norm = Xave/Fave*0.256
Norm_Cold = Norm*20000
Norm_Hot = Norm*60
"""END OF PARAMETERS"""
"""Final Star output"""
"""Final Star output"""
"""START OF DATA FOR HOT DATA CURVE"""
Flux_Hot_N = plank(wave, T_Hot, Norm_Hot)
"""END OF HOT CURVE DATA PLOT INFO"""
"""COLD DATA START PLOT INFO"""
Flux_Cold_N = plank(wave, T_Cold, Norm_Cold)
"""COLD DATA END PLOT INFO"""
"""START OF SUM PLOT CURVE"""
X_sum = []
for i in wave:
    a_sum = plank(i, T, Norm)
    b_sum = plank(i, T_Hot, Norm_Hot)
    c_sum = plank(i, T_Cold, Norm_Cold)
    X_sum.append(a_sum + b_sum + c_sum)
"""END OF SUM PLOT CURVE"""
"""Chi^2 ROUTINE"""
Theo = []
for i in x:
    a_sum = plank(i*1e-6, T, Norm)
    b_sum = plank(i*1e-6, T_Hot, Norm_Hot)
    c_sum = plank(i*1e-6, T_Cold, Norm_Cold)
    Theo.append(a_sum + b_sum + c_sum)
Theory = np.array(Theo)
Obs = np.array(x)
uncert = np.array(z)
Chi = sum(((Obs - Theory)**2)/(uncert**2))
Re_Chi = Chi/(len(x)-4)


"""Chi^2 ROUTINE"""
"""--------------------------------"""
"""--------------------------------"""
"""--------FIRST ITERATION---------"""
"""--------------------------------"""
"""--------------------------------"""
"""FITTING-------THIS MUST MINIMIZE THE CHI VALUE"""
UP = 1.1
DOWN = .9
a = UP

print Re_Chi

T_list = []
Chi_Hold_List = []
count = 0    
while count < 500:
    count += 1
    print count
    Norm *= a
    Theo_Nu = []
    for i in x:
        a_sum = plank(i*1e-6, T, Norm)
        b_sum = plank(i*1e-6, T_Hot, Norm_Hot)
        c_sum = plank(i*1e-6, T_Cold, Norm_Cold)
        Theo_Nu.append(a_sum + b_sum + c_sum)
    Theory_Nu = np.array(Theo_Nu)
    Obs_Nu = np.array(x)
    uncert_Nu = np.array(z)
    Chi_Nu = sum(((Obs_Nu - Theory_Nu)**2)/(uncert_Nu**2))
    Re_Chi_Nu = Chi_Nu/(len(x)-4)
    if a == UP and Re_Chi_Nu < Re_Chi:
        a = UP
    elif a == UP and Re_Chi_Nu > Re_Chi:
        a = DOWN
        
    elif a == DOWN and Re_Chi_Nu < Re_Chi:
        a = DOWN
    elif a == DOWN and Re_Chi_Nu > Re_Chi:
        a = UP
    Re_Chi = Re_Chi_Nu
    

    
"""FITTING-------THIS MUST MINIMIZE THE CHI VALUE"""
"""--------------------------------"""
"""--------------------------------"""
"""--------LAST ITERATION----------"""
"""--------------------------------"""
"""--------------------------------"""
"""STAR PLOT"""
Flux = plank(wave, T, Norm)
"""STAR PLOT"""
"""START OF DATA FOR HOT DATA CURVE"""
Flux_Hot_N = plank(wave, T_Hot, Norm_Hot) 
"""END OF HOT CURVE DATA PLOT INFO"""
"""COLD DATA START PLOT INFO"""
Flux_Cold_N = plank(wave, T_Cold, Norm_Cold)
"""COLD DATA END PLOT INFO"""
"""START OF SUM PLOT CURVE"""
X_sum = []
for i in wave:
    a_sum = plank(i, T, Norm)
    b_sum = plank(i, T_Hot, Norm_Hot)
    c_sum = plank(i, T_Cold, Norm_Cold)
    X_sum.append(a_sum + b_sum + c_sum)
"""END OF SUM PLOT CURVE"""
"""THIS IS THE BEGINNING OF ALL THE PLOT OVERLAYS"""
plt.hold(True)
plt.loglog(wave*1e6, Flux, 'y-') 
plt.loglog(wave*1e6, Flux_Hot_N, 'r-') 
plt.loglog(wave*1e6, Flux_Cold_N, 'b-') 
plt.loglog(x, Theo, 'ro', label='Theory') 
plt.loglog(wave*1e6, X_sum, 'g--', label='Curve Sum') 
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