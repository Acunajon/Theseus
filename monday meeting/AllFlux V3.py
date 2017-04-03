"""
JonathanAcuna
"""


from fitting import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import csv

wave = np.arange(1e-6, 500e-6, 1e-6) 

temp = {
        'batch_list\\Astars_12710400_HD79108_spectra.txt' : 9680,
        'batch_list\\Astars_12720384_HD110411_spectra.txt' : 8540,
        'batch_list\\DDisk_17jun13_allIRflux.txt' : 8870
        }

Values = [['T_Star', 'Norm', 'T_Disk_1', 'Norm_Disk_1', 'T_Disk_2', 'Norm_Disk_2', 'Chi']]
f = getfiles('batch_list')
#d = getfiles('Initial_data/nextgen')
#Nextgen = [s for s in d if (str(temest) + 'g40') in s]
dy = 220
#Opens data file gets data runs fitting stores parameters.
for i in f:
    x, y, z = data(i)
    T_star = temp[i]
    Norm, T_Disk_1, Norm_Disk_1, T_Disk_2, Norm_Disk_2, Chi = fitting(x, y, z, T_star, loop_num=0)
    #makes the list of parameters
    i = []
    i.append(T_star)
    i.append(Norm)
    i.append(T_Disk_1)
    i.append(Norm_Disk_1)
    i.append(T_Disk_2)
    i.append(Norm_Disk_2)
    i.append(Chi)
    Values.append(i)

with open('list.csv', 'wb') as testfile:
    addition = csv.writer(testfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in Values:
        addition.writerow([i])       

    
"""
ax1 = plt.plot()
#uses parameters to plot
for i in Values:
    if i == Values[0]:
        pass
    #Pulls NextGen file for plot
    d = getfiles('nextgen')
    Nextgen = [s for s in d if (str(temper(T_star)) + 'g40') in s]  
    #makes the plots
    Flux_S = planck(wave, i[0], i[1])
    Flux_1 = planck(wave, i[2], i[3])
    Flux_2 = planck(wave, i[4], i[5])
    Flux_Tot = Flux_S + Flux_1 + Flux_2
    #makes the plot
    dy += 1
    plt.hold(True)
    plt.loglog(x,y, 'k.')
    plt.loglog(wave*1e6,Flux_S, 'y-')
    plt.loglog(wave*1e6,Flux_1, 'b-')
    plt.loglog(wave*1e6,Flux_2, 'r-')
    plt.loglog(wave*1e6,Flux_Tot, 'g--')
    #stores plot and parameters for each star
    with open('list.csv', 'wb') as testfile:
        addition = csv.writer(testfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        addition.writerow([i])    
        
        
        
temest = temper(T_star)
Nextgen = [s for s in test if (str(temest) + 'g40') in s]
           
           
           
           
           
           
ax1.show()
           
           """
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           