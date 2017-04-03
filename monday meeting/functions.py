"""
Jonathan Acuna
"""
from constants import *
import os
import numpy as np

#plannk function
def planck(Wav, T=100, Norm=1):
    a = 2*h*c
    b = h*c/(Wav*k*T)
    Flux = (a/Wav**3)*(1/(e**(b)-1))*10**-19*Norm
    return Flux
    
#opens single file and orginizes contents for analysis
def data(f):
    sample1 = open(f, 'r')
    d = np.genfromtxt(f, skip_header=1)
    x = []
    y = []
    z = []
    for i in d:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return x, y, z
    
def data_s(f):
    sample1 = open(f, 'r')
    d = np.genfromtxt(f, skip_header=1)
    x = []
    y = []
    for i in d:
        x.append(i[0])
        y.append(i[1])
    return x, y

#opens directory and cycles through files    
def getfiles(directory):
    files = []
    for filename in os.listdir(directory):
        #x, y, z = data(directory + '\\' + filename)
        files.append(directory + '\\' + filename)
    return files

#takes star temp and finds nearest temp for nextgen model    
def temper(base):
    if (base / 100) % 2 == 0:
        A = (base/100) * 100
    else:
        A = (base/100 +1) * 100
    return A

"""    
def run(d): # d is directory
    for f in os.listdir(d):
        
        #run fucnction on file
        #print data
"""
        
"""       
plt.hold(True)
f = getfiles('batch_list')
for i in f:
    x, y, z = data(i)
    plt.plot(x,y)
plt.show()
"""