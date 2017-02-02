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
T = 10000

def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)+1))*Conv
    return Flux
        
print 4



#print plank(x, T)

print 4.1

Wavel = []

wave = np.arange(1e-9, 500e-6, 1e-7) 
#wave = np.arange(min(x), max(x), 1e-6) 

for i in wave:
    Wavel.append(i)
    
    
    
print len(wave)


print 4.2



Flux = plank(wave, T)





print 4.25


print 'first 4 of x'
print x[0:4]

print 4.3

print 'first 4 flux values'
print Flux[0:4]

print 4.4

Xave=sum(x[0:4])/5
Fave=sum(Flux[0:4])/5

#print Fave

#F2=Flux[Xave]
print 4.45

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
    

print 4.5
""
plt.hold(True)
#plt.plot(wave*1e6, Flux, 'r-') 

plt.loglog(wave*1e6, FluxN, 'y-') 
#plt.loglog(wave, FluxN, 'r-') 
""
print 5
""
plt.loglog(x,y,'b.')
plt.show()
plt.ylabel('Flux (Jy)')
plt.xlabel('Wavelength (microns)')
""
print 5.5

be = wave[0]
fin = wave[len(wave)-1]

print be
print fin

""
#plt.xlim([be,fin])
#plt.ylim([0.01,10])
""

print 6



"""
np.log is ln, whereas np.log10 is your standard base 10 log.
plt.loglog   plots with axis in log vs log.
"""