"""
JonathanAcuna
"""

#fitting(wave, value, sigma, T_star, loop_num=1000):
#planck(Wav, T=100, Norm=1):
from functions import *
from fitting import *
#data(directory) getfiles(directory)

import numpy as np
import matplotlib.pyplot as plt
import csv

temp = {
        'batch_list\\Astars_12710400_HD79108_spectra.txt' : 9680,
        'batch_list\\Astars_12720384_HD110411_spectra.txt' : 8540,
        'batch_list\\DDisk_17jun13_allIRflux.txt' : 8870
        }

        
d = getfiles('TEST')
x, y, z = data(d[0])
X, Y = data_s(d[1])
X_Nu = np.array(X)
Y_Nu = np.array(Y)

Norm, T_Disk_1, Norm_Disk_1, T_Disk_2, Norm_Disk_2, Chi = fitting(x, y, z, 8870, loop_num=0)
wave = np.arange(1e-6, 500e-6, 1e-6) 

Flux = planck(wave, 8870, Norm)
Flux_1 = planck(wave, T_Disk_1, Norm_Disk_1)
Flux_2 = planck(wave, T_Disk_2, Norm_Disk_2)
Flux_Tot = Flux + Flux_1 + Flux_2

plt.hold(True)

plt.loglog(x,y, 'k.')
plt.loglog(X_Nu*1e-6,Y_Nu*Norm, 'b.')
#plt.loglog(wave*1e6,Flux, 'b-')
plt.loglog(wave*1e6,Flux_1, 'b-')
plt.loglog(wave*1e6,Flux_2, 'r-')
plt.loglog(wave*1e6,Flux_Tot, 'g--')


plt.show()









"""

T_star = 9090

temest = temper(T_star)
Nextgen = [s for s in d if (str(temest) + 'g40') in s]
print Nextgen

test = ['8600g45.txt', '8600g40.txt', '8600g45.txt', '8800g45.txt', '8800g40.txt', '9000g45.txt', '9000g40.txt', '9200g45.txt']
base = [9090, 5678, 3456, 9786,6789, 5678,8756]

for i in base:
    temp = temper(i)
    matching = [s for s in test if (str(temp) + 'g40') in s]
    print matching

'$' in s        # found
'$' not in s    # not found

# original answer given, but less Pythonic than the above...
s.find('$')==-1 # not found
s.find('$')!=-1 # found



temp = {
        'batch_list\\Astars_12710400_HD79108_spectra.txt' : 9680,
        'batch_list\\Astars_12720384_HD110411_spectra.txt' : 8540,
        'batch_list\\DDisk_17jun13_allIRflux.txt' : 8870
        }

Values = [['T_Star', 'Norm', 'T_Disk_1', 'Norm_Disk_1', 'T_Disk_2', 'Norm_Disk_2', 'Chi']]
f = getfiles('batch_list')
a = 110
for i in f:
    a +=1
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
    
    #makes the plots
    Flux_S = planck(wave, i[0], i[1])
    Flux_1 = planck(wave, i[2], i[3])
    Flux_2 = planck(wave, i[4], i[5])
    Flux_Tot = Flux_S + Flux_1 + Flux_2
    
    #makes the plot
    plt.subplot(a)
    plt.loglog(x,y, 'k.')
    plt.loglog(wave*1e6,Flux_S, 'y-')
    plt.loglog(wave*1e6,Flux_1, 'b-')
    plt.loglog(wave*1e6,Flux_2, 'r-')
    plt.loglog(wave*1e6,Flux_Tot, 'g--')
    plt.xlim([0.1,520])
    plt.ylim([0.0000001,100])
    
    #adds table to plot
#    columns = ( 'T_Star', 'Norm', 'T_Disk_1', 'Norm_Disk_1', 'T_Disk_2', 'Norm_Disk_2', 'Chi')
#    the_table = ax1.table(rowLabels='Parameters', colLabels=columns,loc='bottom')
    #stores plot and parameters for each star


with open('parameters.csv', 'wb') as testfile:
    addition = csv.writer(testfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in Values:
        addition.writerow([i])        
    
fig = plt.figure()

x = [1,5,3,5,7,1]
y = [5,3,1,2,5,7]
z = [7,3,5,1,3,6]
al = [x,y,z]


a = 220
for i in range(4):
    a += 1
        
    ax = fig.add_subplot(a)
    ax.plot(x,y,'k.')
  
plt.show()
    
    ax = fig.add_subplot(a)
    ax.plot(x,z,'k.')
    
    ax = fig.add_subplot(a)
    ax.plot(z,y,'k.')
    
    ax = fig.add_subplot(a)
    ax.plot(z,x,'k.')

Values = [['Norm', 'T_Disk_1', 'Norm_Disk_1', 'T_Disk_2', 'Norm_Disk_2', 'Chi']]
f = getfiles('batch_list')
for i in f:
    x, y, z = data(i)
    Norm, T_Disk_1, Norm_Disk_1, T_Disk_2, Norm_Disk_2, Chi = fitting(x, y, z, 8870, loop_num=0)
    i = []
    i.append(Norm)
    i.append(T_Disk_1)
    i.append(Norm_Disk_1)
    i.append(T_Disk_2)
    i.append(Norm_Disk_2)
    i.append(Chi)
    Values.append(i)
    
import csv
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])    

    
with open('list.csv', 'wb') as testfile:
    addition = csv.writer(testfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in Values:
        addition.writerow([i])


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

    
Flux_S = planck(wave,T_star, Norm)
Flux_1 = planck(wave, T_Disk_1, Norm_Disk_1)
Flux_2 = planck(wave, T_Disk_2, Norm_Disk_2)
Flux_Tot = Flux_S + Flux_C + Flux_H


plt.hold(True)
plt.loglog(wave*1e6,Flux_S, 'y-')
plt.loglog(wave*1e6,Flux_C, 'b-')
plt.loglog(wave*1e6,Flux_H, 'r-')
plt.loglog(wave*1e6,Flux_Tot, 'g--')
plt.loglog(x,y, 'k.')
plt.errorbar(x,y,yerr=z,linestyle="none")


plt.title('20')
plt.xlim([0.1,520])
plt.ylim([0.0000001,100])


plt.show()

"""