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
X = np.array(x)
Y = np.array(y)
Z = np.array(z)
"""DESIRED DATA FILE"""
"""WAVE LENGTH RANGE"""
wave = np.arange(1e-6, 500e-6, 1e-6) 
"""WAVE LENGTH RANGE"""
"""PLANK FUNCTION"""
def planck(Wav, T=100, Norm=1):
    a = 2*h*c
    b = h*c/(Wav*k*T)
    Flux = (a/Wav**3)*(1/(e**(b)-1))*10**-19*Norm
    return Flux
"""PLANK FUNCTION END"""
"""STAR VALUES"""
T_star = 10000
"""STAR VALUES"""
"""INITIAL FLUX OUTPUTS"""
Flux_S = planck(wave,T_star)
Flux_C = planck(wave)
Flux_H = planck(wave)
Flux_Tot = Flux_S + Flux_C + Flux_H
"""INITIAL FLUX OUTPUTS"""
"""INITIAL CHI VALUE"""
result = []
for i in x:
    Star = planck(i*1e-6, T_star)
    Cold = planck(i*1e-6)
    Hot = planck(i*1e-6)
    result.append(Star + Cold + Hot)
Result = np.array(result)
Chi = sum(((Result - Y)**2)/(Z**2))
Re_Chi = Chi/(len(x)-4)
"""INITIAL CHI VALUE"""
"""PARAMETERS TO BE OPTIMIZED"""
Norm = 1
T_cold = 100
Norm_cold = 1
T_hot = 100
Norm_hot = 1
para = [Norm, T_cold, Norm_cold, T_hot, Norm_hot]
"""PARAMETERS TO BE OPTIMIZED"""
"""OPTIMIZATION ROUTINE"""

UP = 1.1
DOWN = .9
a = UP
a_list = []
Norm_List = []
Chi_List = []
count = 0
while count < 1000:
    count += 1
    Norm *= a
    Flux = []
    Star = planck(x[0]*1e-6, T_star, Norm)
    Flux.append(Star)
    Chi_Norm = (((Flux[0]-y[0])**2)/(z[0]**2))
    Chi_loop = Chi_Norm/(len(x)-4)
    Chi_List.append(Chi_loop)
    if a == UP and Chi_loop < Re_Chi:
        a = UP
    elif a == UP and Chi_loop > Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop > Re_Chi:
        a = UP
    a_list.append(a)
    Re_Chi = Chi_loop
    Norm_List.append(Norm)

    
UP = 1.1
DOWN = .9
a = UP
a_list = []
Norm_List = []
Chi_List = []
count = 0
while count < 1000:
    count += 1
    Norm_cold *= a
    Flux = []
    Cold = planck(x[231]*1e-6, T_cold, Norm_cold)
    Flux.append(Cold)
    Chi_Norm = (((Flux[0]-y[0])**2)/(z[0]**2))
    Chi_loop = Chi_Norm/(len(x)-4)
    Chi_List.append(Chi_loop)
    if a == UP and Chi_loop < Re_Chi:
        a = UP
    elif a == UP and Chi_loop > Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop > Re_Chi:
        a = UP
    a_list.append(a)
    Re_Chi = Chi_loop
    Norm_List.append(Norm_cold)

    
    
""" 

UP = 1.1
DOWN = .9
a = UP
a_list = []
Norm_List = []
Chi_List = []
count = 0
while count < 1000:
    count += 1
    T_cold *= a
    Flux = []
    for i in x:
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        Flux.append(Star + Cold+ Hot)
    Chi_Norm =(((Flux[231]-y[231])**2)/(z[231]**2))
    Chi_loop = Chi_Norm/(len(x)-4)
    Chi_List.append(Chi_loop)
    if a == UP and Chi_loop < Re_Chi:
        a = UP
    elif a == UP and Chi_loop > Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop > Re_Chi:
        a = UP
    a_list.append(a)
    Re_Chi = Chi_loop
    Norm_List.append(T_cold) 
    
    
UP = 1.1
DOWN = .9
a = UP
a_list = []
Norm_List = []
Chi_List = []
count = 0
while count < 500:
    count += 1
    Norm_hot *= a
    Flux = []
    for i in x:
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        Flux.append(Star + Cold+ Hot)
    Chi_Norm = []
    for i in range(len(x)):
        Chi_Norm.append(((Flux[i]-y[i])**2)/(z[i]**2))
    Chi_loop = sum(Chi_Norm)/(len(x)-4)
    Chi_List.append(Chi_loop)
    if a == UP and Chi_loop < Re_Chi:
        a = UP
    elif a == UP and Chi_loop > Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop > Re_Chi:
        a = UP
    a_list.append(a)
    Re_Chi = Chi_loop
    Norm_List.append(Norm_hot)
    
    
UP = 1.1
DOWN = .9
a = UP
a_list = []
Norm_List = []
Chi_List = []
count = 0
while count < 500:
    count += 1
    T_hot *= a
    Flux = []
    for i in x:
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        Flux.append(Star + Cold+ Hot)
    Chi_Norm = []
    for i in range(len(x)):
        Chi_Norm.append(((Flux[i]-y[i])**2)/(z[i]**2))
    Chi_loop = sum(Chi_Norm)/(len(x)-4)
    Chi_List.append(Chi_loop)
    if a == UP and Chi_loop < Re_Chi:
        a = UP
    elif a == UP and Chi_loop > Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Chi_loop > Re_Chi:
        a = UP
    a_list.append(a)
    Re_Chi = Chi_loop
    Norm_List.append(T_hot)

    
"""
    
    
    
    
"""INITIAL FLUX OUTPUTS"""
Flux_S = planck(wave,T_star, Norm)
Flux_C = planck(wave, T_cold, Norm_cold)
Flux_H = planck(wave, T_hot, Norm_hot)
Flux_Tot = Flux_S + Flux_C + Flux_H
"""INITIAL FLUX OUTPUTS"""


plt.hold(True)
plt.loglog(wave*1e6,Flux_S, 'y-')
plt.loglog(wave*1e6,Flux_C, 'b-')
plt.loglog(wave*1e6,Flux_H, 'r-')
plt.loglog(wave*1e6,Flux_Tot, 'g--')
plt.loglog(x,y, 'k.')
plt.show()