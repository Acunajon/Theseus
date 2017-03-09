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
"""PARAMETERS TO BE OPTIMIZED"""
"""OPTIMIZATION ROUTINE"""
"""LISTS"""
Chi_list_Norm = []#                                                            CHI LIST NORM
Norm_list = []#                             PARAMETER   NORM                   NORM LIST
a_Norm_list = []#                                                              A LIST NORM

Chi_list_Norm_cold = []#                                                       CHI LIST NORM COLD
Norm_cold_list = []#                        PARAMETER   NORM COLD              NORM COLD LIST
a_Norm_cold_list = []#                                                         A NORM COLD LIST

Chi_list_T_COLD = []#                                                          CHI LIST T COLD
T_cold_list = []#                           PARAMETER   T COLD                 T COLD
a_T_cold_list = []#                                                            A T COLD LIST

Chi_list_NORM_HOT = []#                                                        CHI LIST NORM HOT
Norm_HOT_list = []#                         PARAMETER   NORM HOT               NORM HOT LIST
a_NORM_HOT_LIST = []#                                                          A NORM HOT

Chi_list_T_HOT = []#                                                           T HOT CHI LIST
list_T_HOT = []#                            PARAMETER   T HOT                  T HOT LIST
a_T_HOT_LIST = []#                                                             A T HOT LIST




"""-----------------------------------"""
loop = 0
while loop < 1000:
    loop += 1
    print loop
    
    result = []#                                                               NORM
    for i in x:
        Star = planck(i*1e-6, T_star, Norm)
        Cold = planck(i*1e-6, T_cold, Norm_cold)
        Hot = planck(i*1e-6, T_hot, Norm_hot)
        result.append(Star + Cold + Hot)
    Result = np.array(result)
    Chi_Norm = sum(((Result - Y)**2)/(Z**2))
    Re_Chi_Norm = Chi_Norm/(len(x)-4)
    
    
    UP = 1.1
    DOWN = 0.9
    a = UP
    count = 0                                   
    while count < 10:                           
        count += 1
        Norm *= a
        Norm_list.append(Norm)
        result_loop_Norm = []#                                                 RESULT LIST
        for i in x:                                       
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result_loop_Norm.append(Star + Cold + Hot)
        Result_LOOP_NORM = np.array(result_loop_Norm)
        Chi_Norm = sum(((Result_LOOP_NORM - Y)**2)/(Z**2))
        Re_Chi_loop_Norm = Chi_Norm/(len(x)-4)
        
        if a == UP and Re_Chi_loop_Norm < Re_Chi_Norm:                
            a = UP
        elif a == UP and Re_Chi_loop_Norm > Re_Chi_Norm:
            a = DOWN
        elif a == DOWN and Re_Chi_loop_Norm < Re_Chi_Norm:
            a = DOWN
        elif a == DOWN and Re_Chi_loop_Norm > Re_Chi_Norm:
            a = UP
        
        Chi_list_Norm.append(Re_Chi_loop_Norm)
        a_Norm_list.append(a)
        Re_Chi_Norm = Re_Chi_loop_Norm                             
      
        
        
    result = []#                                                               NORM COLD
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
    count = 0                                  
    while count < 10:                            
        count += 1
        Norm_cold *= a
        Norm_cold_list.append(Norm_cold)
        result_loop_Norm_cold = []#                                            RESULT LIST NORM COLD
        for i in x:                                      
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result_loop_Norm_cold.append(Star + Cold + Hot)
        Result = np.array(result_loop_Norm_cold)
        Chi_Norm = sum(((Result - Y)**2)/(Z**2))
        Re_Chi_loop = Chi_Norm/(len(x)-4)

        if a == UP and Re_Chi_loop < Re_Chi:                
            a = UP
        elif a == UP and Re_Chi_loop > Re_Chi:
            a = DOWN
        elif a == DOWN and Re_Chi_loop < Re_Chi:
            a = DOWN
        elif a == DOWN and Re_Chi_loop > Re_Chi:
            a = UP
    
        Chi_list_Norm_cold.append(Re_Chi_loop)
        a_Norm_cold_list.append(a)
        Re_Chi = Re_Chi_loop


        
    result = []#                                                               T COLD
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
    count = 0
    while count < 10:
        count += 1
        T_cold *= a
        T_cold_list.append(T_cold)

        
        Cold = planck(x[231]*1e-6, T_cold, Norm_cold)
        
        Chi = (((Cold - y[231])**2)/(z[231]**2))
    
        if a == UP and Chi < Re_Chi:
            a = UP
        elif a == UP and Chi > Re_Chi:
            a = DOWN
        
        elif a == DOWN and Chi < Re_Chi:
            a = DOWN
        elif a == DOWN and Chi > Re_Chi:
            a = UP
        
        Chi_list_T_COLD.append(Chi)
        T_cold_list.append(T_cold)
        Chi = Re_Chi

        
    
    
    
    
    
        
    result = []#                                                               NORM HOT
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
    count = 0
    while count < 10:
        count += 1
        Norm_hot *= a
        Norm_HOT_list.append(Norm_hot)
        result_loop = []#                                                      RESULT NORM HOT
        for i in x:
            Star = planck(i*1e-6, T_star, Norm)
            Cold = planck(i*1e-6, T_cold, Norm_cold)
            Hot = planck(i*1e-6, T_hot, Norm_hot)
            result_loop.append(Star + Cold + Hot)
        Result = np.array(result_loop)
        Chi_Norm = sum(((Result - Y)**2)/(Z**2))
        Re_Chi_loop = Chi_Norm/(len(x)-4)

        if a == UP and Re_Chi_loop < Re_Chi:               
            a = UP
        elif a == UP and Re_Chi_loop > Re_Chi:
            a = DOWN
        elif a == DOWN and Re_Chi_loop < Re_Chi:
            a = DOWN
        elif a == DOWN and Re_Chi_loop > Re_Chi:
            a = UP
    
        Chi_list_NORM_HOT.append(Re_Chi_loop)
        a_NORM_HOT_LIST.append(a)
        Re_Chi = Re_Chi_loop   

        
#    result = []#                                                               T HOT
#    for i in x:
#        Star = planck(i*1e-6, T_star, Norm)
#        Cold = planck(i*1e-6, T_cold, Norm_cold)
#        Hot = planck(i*1e-6, T_hot, Norm_hot)
#        result.append(Star + Cold + Hot)
#    Result = np.array(result)
#    Chi = sum(((Result - Y)**2)/(Z**2))
#    Re_Chi = Chi/(len(x)-4)

#    UP = 1.1
#    DOWN = 0.9
#    a = UP
#    count = 0
#    while count < 10:
#        count += 1
#        T_hot *= a
#        list_T_HOT.append(T_hot)
#        result_loop = []#                                                      RESULT T HOT
#        for i in x:
#            Star = planck(i*1e-6, T_star, Norm)
#            Cold = planck(i*1e-6, T_cold, Norm_cold)
#            Hot = planck(i*1e-6, T_hot, Norm_hot)
#            result_loop.append(Star + Cold + Hot)
#        Result = np.array(result_loop)
#        Chi_Norm = sum(((Result - Y)**2)/(Z**2))
#        Re_Chi_loop = Chi_Norm/(len(x)-4)

#        if a == UP and Re_Chi_loop < Re_Chi:
#            a = UP
#        elif a == UP and Re_Chi_loop > Re_Chi:
#            a = DOWN
#        elif a == DOWN and Re_Chi_loop < Re_Chi:
#            a = DOWN
#        elif a == DOWN and Re_Chi_loop > Re_Chi:
#            a = UP
        
#        a_T_HOT_LIST.append(a)
#        Chi_list_T_HOT.append(Re_Chi_loop)
#        Re_Chi = Re_Chi_loop 

        
"""

    UP = 1.1
    DOWN = 0.9
    a = UP
    count = 0                                                        
    while count < 10:                            
        count += 1
        Norm *= a
        
        Star = planck(x[0]*1e-6, T_star, Norm)

        if a == UP and Star < y[0]:                    
            a = UP
        elif a == UP and Star > y[0]:
            a = DOWN
        
        elif a == DOWN and Star < y[0]:
            a = DOWN
        elif a == DOWN and Star > y[0]:
            a = UP

    UP = 1.1
    DOWN = 0.9
    a = UP                           
    count = 0                                                                      
    while count < 10:                        
        count += 1
        Norm_cold *= a    
                                       
        Cold = planck(x[231]*1e-6, T_cold, Norm_cold)

        if a == UP and Cold < y[231]:               
            a = UP
        elif a == UP and Cold > y[231]:
            a = DOWN
        
        elif a == DOWN and Cold < y[231]:
            a = DOWN
        elif a == DOWN and Cold > y[231]:
            a = UP
"""    
 
 
 
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
plt.errorbar(x,y,yerr=z,linestyle="none")

"""PLOT LIMITS"""
plt.xlim([0.1,520])
plt.ylim([0.0000001,100])
"""PLOT LIMITS"""



plt.show()