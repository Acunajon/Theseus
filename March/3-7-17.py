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
"""  EXAMPLE
UP = 1.1
DOWN = .9
a = UP
T_OFF = 5
Chi_1 = (((T - T_GOAL)**2)/(T_OFF**2))
Chi_List = []
count = 0
T_Nu = []
while count < 500:
    count += 1
    print count
    T *= a
    T_Nu.append(T)
    
    Chi = (((T - T_GOAL)**2)/(T_OFF**2))
    Chi_List.append(Chi)
    
    if a == UP and Chi < Chi_1:
        a = UP
    elif a == UP and Chi > Chi_1:
        a = DOWN
        
    elif a == DOWN and Chi < Chi_1:
        a = DOWN
    elif a == DOWN and Chi > Chi_1:
        a = UP
        
    T_List.append(T)
    Chi_1 = Chi
"""
result = []
for i in x:
    Star = planck(i*1e-6, T_star)
    Cold = planck(i*1e-6)
    Hot = planck(i*1e-6)
    result.append(Star + Cold + Hot)
Result = np.array(result)
Chi = sum(((Result - Y)**2)/(Z**2))
Re_Chi = Chi/(len(x)-4)

UP = 1.1
DOWN = 0.9
a = UP
Sigma = z
Chi_list = []                                #    NORM
count = 0                                    #    NORM
Norm_list = []                               #    NORM
while count < 1000:                          #    NORM
    count += 1
    Norm *= a
    Norm_list.append(Norm)
    result_loop = []
    for i in x:                                       #  CALCULATES CHI FOR IN LOOP
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6)
        Hot = planck(i*1e-6)
        result_loop.append(Star + Cold + Hot)
    Result_loop = np.array(result_loop)
    Chi_loop = sum(((Result_loop - Y)**2)/(Z**2))
    Re_Chi_loop = Chi_loop/(len(x)-4)

    if a == UP and Re_Chi_loop < Re_Chi:                #   ALTERS THE MULTIPLIER FOR FITTING
        a = UP
    elif a == UP and Re_Chi_loop > Re_Chi:
        a = DOWN
        
    elif a == DOWN and Re_Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Re_Chi_loop > Re_Chi:
        a = UP
    
    Re_Chi = Re_Chi_loop                             #   STORES CHI_loop FOR NEXT LOOP ITERATION
""" NORM IS NOW FITTED"""
"""----------------------------------"""
"""----------------------------------"""
"""-------BEGIN NEXT PARAMETER-------"""
"""----------------------------------"""
"""----------------------------------"""
""" NORM COLD FOR OUTER BELT """
result = []
for i in x:
    Star = planck(i*1e-6, T_star, Norm)
    Cold = planck(i*1e-6, T_cold, Norm_cold)
    Hot = planck(i*1e-6)
    result.append(Star + Cold + Hot)
Result = np.array(result)
Chi = sum(((Result - Y)**2)/(Z**2))
Re_Chi = Chi/(len(x)-4)

UP = 1.1
DOWN = 0.9
a = UP
Sigma = z
Chi_list = []                                #    NORM_COLD
count = 0                                    #    NORM_COLD
Norm_list = []                               #    NORM_COLD
while count < 1000:                          #    NORM_COLD
    count += 1
    Norm_cold *= a
    Norm_list.append(Norm)
    result_loop = []
    for i in x:                                       #  CALCULATES CHI FOR IN LOOP
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6)
        result_loop.append(Star + Cold + Hot)
    Result_loop = np.array(result_loop)
    Chi_loop = sum(((Result_loop - Y)**2)/(Z**2))
    Re_Chi_loop = Chi_loop/(len(x)-4)

    if a == UP and Re_Chi_loop < Re_Chi:                #   ALTERS THE MULTIPLIER FOR FITTING
        a = UP
    elif a == UP and Re_Chi_loop > Re_Chi:
        a = DOWN
        
    elif a == DOWN and Re_Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Re_Chi_loop > Re_Chi:
        a = UP
    
    Re_Chi = Re_Chi_loop   

"""--------------------------------"""
    
result = []
for i in x:
    Star = planck(i*1e-6, T_star, Norm)
    Cold = planck(i*1e-6, T_cold, Norm_cold)
    Hot = planck(i*1e-6)
    result.append(Star + Cold + Hot)
Result = np.array(result)
Chi = sum(((Result - Y)**2)/(Z**2))
Re_Chi = Chi/(len(x)-4)

UP = 1.1
DOWN = 0.9
a = UP
Sigma = z
Chi_list = []                                #    NORM_COLD
count = 0                                    #    NORM_COLD
Norm_list = []                               #    NORM_COLD
while count < 1000:                          #    NORM_COLD
    count += 1
    T_cold *= a
    Norm_list.append(Norm)
    result_loop = []
    for i in x:                                       #  CALCULATES CHI FOR IN LOOP
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6)
        result_loop.append(Star + Cold + Hot)
    Result_loop = np.array(result_loop)
    Chi_loop = sum(((Result_loop - Y)**2)/(Z**2))
    Re_Chi_loop = Chi_loop/(len(x)-4)

    if a == UP and Re_Chi_loop < Re_Chi:                #   ALTERS THE MULTIPLIER FOR FITTING
        a = UP
    elif a == UP and Re_Chi_loop > Re_Chi:
        a = DOWN
        
    elif a == DOWN and Re_Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Re_Chi_loop > Re_Chi:
        a = UP
    
    Re_Chi = Re_Chi_loop 

"""----------------------------------"""
    
result = []
for i in x:
    Star = planck(i*1e-6, T_star, Norm)
    Cold = planck(i*1e-6, T_cold, Norm_cold)
    Hot = planck(i*1e-6, T_hot, Norm_hot)
    result.append(Star + Cold + Hot)
Result = np.array(result)
Chi = sum(((Result - Y)**2)/(Z**2))
Re_Chi = Chi/(len(x)-4)

UP = 1.1
DOWN = 0.9
a = UP
Sigma = z
Chi_list = []                                #    NORM_COLD
count = 0                                    #    NORM_COLD
Norm_list = []                               #    NORM_COLD
while count < 1000:                          #    NORM_COLD
    count += 1
    Norm_hot *= a
    Norm_list.append(Norm)
    result_loop = []
    for i in x:                                       #  CALCULATES CHI FOR IN LOOP
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        result_loop.append(Star + Cold + Hot)
    Result_loop = np.array(result_loop)
    Chi_loop = sum(((Result_loop - Y)**2)/(Z**2))
    Re_Chi_loop = Chi_loop/(len(x)-4)

    if a == UP and Re_Chi_loop < Re_Chi:                #   ALTERS THE MULTIPLIER FOR FITTING
        a = UP
    elif a == UP and Re_Chi_loop > Re_Chi:
        a = DOWN
        
    elif a == DOWN and Re_Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Re_Chi_loop > Re_Chi:
        a = UP
    
    Re_Chi = Re_Chi_loop   

"""-------------------------------------"""
    
result = []
for i in x:
    Star = planck(i*1e-6, T_star, Norm)
    Cold = planck(i*1e-6, T_cold, Norm_cold)
    Hot = planck(i*1e-6, T_hot, Norm_hot)
    result.append(Star + Cold + Hot)
Result = np.array(result)
Chi = sum(((Result - Y)**2)/(Z**2))
Re_Chi = Chi/(len(x)-4)

UP = 1.1
DOWN = 0.9
a = UP
Sigma = z
Chi_list = []                                #    NORM_COLD
count = 0                                    #    NORM_COLD
Norm_list = []                               #    NORM_COLD
while count < 1000:                          #    NORM_COLD
    count += 1
    T_hot *= a
    Norm_list.append(Norm)
    result_loop = []
    for i in x:                                       #  CALCULATES CHI FOR IN LOOP
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        result_loop.append(Star + Cold + Hot)
    Result_loop = np.array(result_loop)
    Chi_loop = sum(((Result_loop - Y)**2)/(Z**2))
    Re_Chi_loop = Chi_loop/(len(x)-4)

    if a == UP and Re_Chi_loop < Re_Chi:                #   ALTERS THE MULTIPLIER FOR FITTING
        a = UP
    elif a == UP and Re_Chi_loop > Re_Chi:
        a = DOWN
        
    elif a == DOWN and Re_Chi_loop < Re_Chi:
        a = DOWN
    elif a == DOWN and Re_Chi_loop > Re_Chi:
        a = UP
    
    Re_Chi = Re_Chi_loop 

    
"""OPTIMIZATION ROUTINE"""
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