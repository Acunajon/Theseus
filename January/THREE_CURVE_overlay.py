"""
JonathanAcuna
"""

print 1


import math
import numpy as np
import matplotlib.pyplot as plt

#import modules
sample1 = open('C:\Users\jma48203\Desktop\Thesis\Initial data\DDisk_17jun13_allIRflux.txt' , 'r')
#calls document by directory
s1=sample1.readlines()
#reads line by line
s1 = np.array(map(lambda x: x.strip(), s1))
#removes whitespace
d = np.array(map(lambda x: x.split(), s1)).reshape((-1,3))
#splits each string into 3 strings
d = np.delete(d, [0,1,2]).reshape((-1,3))
#removes titles
d = d.astype(float)
#makes stings into a decimals

print 2

x = []
y = []

for i in d:
    x.append(i[0])
    y.append(i[1])
    
print 3

pi = math.pi
e = math.e
h = 6.62607004*10**(-34)          #m**2*kg/s
k = 1.38064852*10**(-23)          #m**2*kg/(s**2*K)
c = 299792458   



"""PLANK FUNCTION"""
def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)+1))*Conv
    return Flux
"""PLANK FUNCTION END"""
    
    
print 4



#print plank(x, T)

print 4.1

Wavel = []

wave = np.arange(1e-9, 500e-6, 1e-7) 
#wave = np.arange(min(x), max(x), 1e-6) 

for i in wave:
    Wavel.append(i)
    
    
    
#print len(wave)
print 4.2


"""THIS IS THE BEGINNING FOR THE STAR PLOT"""
T = 10000
Flux = plank(wave, T)
print x[0:4]
print Flux[0:4]
Xave=sum(x[0:4])/5
Fave=sum(Flux[0:4])/5
loop1 = 0
while Xave != Fave:
    Xave=sum(x[0:4])/5
    Fave=sum(Flux[0:4])/5
    Norm = Xave/Fave
    FluxN = Flux*Norm
    loop1 += 1
    if (Xave/Fave)*100 <1 or loop1 == 100:
        print loop1
        break
"""END OF STAR DATA FOR STAR PLOT"""


"""START OF DATA FOR HOT DATA CURVE"""
T_Hot = 235
Flux_Hot = plank(wave, T_Hot)
Flux_Hot_N = Flux_Hot*Norm*10


"""END OF HOT CURVE DATA PLOT INFO"""

"""COLD DATA START PLOT INFO"""
T_Cold = 60
Flux_Cold = plank(wave, T_Cold)
Flux_Cold_N = Flux_Cold*Norm*20000


"""COLD DATA END PLOT INFO"""


print 4.5
""

"""THIS IS THE BEGINNING OF ALL THE PLOT OVERLAYS"""
plt.hold(True)
plt.loglog(wave*1e6, FluxN, 'y-') 
plt.loglog(wave*1e6, Flux_Hot_N, 'r-') 
plt.loglog(wave*1e6, Flux_Cold_N, 'b-') 
plt.loglog(x,y,'k.')
print 5

"""AXIS AND LABELS"""
plt.show()
plt.ylabel('Flux (Jy)')
plt.xlabel('Wavelength (microns)')
"""END OF ALL PLOT LINES"""
print 5.5

""
#plt.xlim([be,fin])
plt.ylim([0.0000001,100])
""

print 6



"""
np.log is ln, whereas np.log10 is your standard base 10 log.
plt.loglog   plots with axis in log vs log.
"""