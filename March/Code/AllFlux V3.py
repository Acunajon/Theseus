"""
JonathanAcuna
"""


from fitting import *
#fitting(wave, value, sigma, T_star, loop_num=1000):
from planck import *
#planck(Wav, T=100, Norm=1):
from preprocess import *
#data(directory) getfiles(directory)

import numpy as np
import matplotlib.pyplot as plt

wave = np.arange(1e-6, 500e-6, 1e-6) 

temp = {
        'batch_list\\Astars_12710400_HD79108_spectra.txt' : 9680,
        'batch_list\\Astars_12720384_HD110411_spectra.txt' : 8540,
        'batch_list\\DDisk_17jun13_allIRflux.txt' : 8870
        }

Values = [['T_Star', 'Norm', 'T_Disk_1', 'Norm_Disk_1', 'T_Disk_2', 'Norm_Disk_2', 'Chi']]
f = getfiles('batch_list')
for i in f:
    x, y, z = data(i)
    T_star = temp[i]
    Norm, T_Disk_1, Norm_Disk_1, T_Disk_2, Norm_Disk_2, Chi = fitting(x, y, z, T_star, loop_num=1)
    i = []
    i.append(T_star)
    i.append(Norm)
    i.append(T_Disk_1)
    i.append(Norm_Disk_1)
    i.append(T_Disk_2)
    i.append(Norm_Disk_2)
    i.append(Chi)
    Values.append(i)

    
    
"""

for i in range(len(Values)):
    if i == 0:
        pass
    Flux_S = planck(wave,Values[i][0], Values[i][1])
    Flux_1 = planck(wave, Values[i][2], Values[i][3])
    Flux_2 = planck(wave, Values[i][4], Values[i][5])
    Flux_Tot = Flux_S + Flux_C + Flux_H
    i = plt.figure()
    ax1 = i.add_subplot(111)
    ax1.loglog(wave*1e6,Flux_S, 'y-')
    ax1.loglog(wave*1e6,Flux_C, 'b-')
    ax1.loglog(wave*1e6,Flux_H, 'r-')
    ax1.loglog(wave*1e6,Flux_Tot, 'g--')
  """  
    
#"""OPTIMIZATION ROUTINE"""
#"""INITIAL FLUX OUTPUTS"""
#Flux_S = planck(wave,T_star, Norm)
#Flux_1 = planck(wave, T_Disk_1, Norm_Disk_1)
#Flux_2 = planck(wave, T_Disk_2, Norm_Disk_2)
#Flux_Tot = Flux_S + Flux_C + Flux_H
#"""INITIAL FLUX OUTPUTS"""


#plt.hold(True)
#plt.loglog(wave*1e6,Flux_S, 'y-')
#plt.loglog(wave*1e6,Flux_C, 'b-')
#plt.loglog(wave*1e6,Flux_H, 'r-')
#plt.loglog(wave*1e6,Flux_Tot, 'g--')
#plt.loglog(x,y, 'k.')
#plt.errorbar(x,y,yerr=z,linestyle="none")



#plt.title('20')
#"""PLOT LIMITS"""
#plt.xlim([0.1,520])
#plt.ylim([0.0000001,100])
#"""PLOT LIMITS"""



plt.show()
