"""This code is supposed to call the data and plot a BB curve on the same plot"""


import numpy as np
import matplotlib.pyplot as plt
import math
#import modules

#bug test
print 1


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
print d


x = []
y = []
for i in d:
    x.append(i[0])
    y.append(i[1])
    
#bug test
print 2

#constants
pi = math.pi
e = math.e
#h = sp.hbar
h = 6.62607004*10**(-34)          #m**2*kg/s
#k = sp.Stefan_Boltzman
k = 1.38064852*10**(-23)          #m**2*kg/(s**2*K)
#c = sp.c
c = 299792458                     #m/s


Wv = 10.0560000
Flx = 0.152130000
T = 10000

#bug test
print 3
#Main function
def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Flux = (a/Wav**5)*(1/(e**(b)+1))
    return Flux
        
    
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 
FluxT = plank(wavelengths, T)/100000000000000

sa = 0
conv = 3.34e-57
a = max(FluxT)
b = plank(a, T)
n = conv*(b**2)


"""

while x[0] != FluxT[x[0]]:
    if abs(x[0] - FluxT[x[0]]) > 10000:
        n = n / 10000
        sa = sa - 1
        print sa
        print 'a'
    elif abs(x[0] - FluxT[x[0]]) < 10000:
        n = n * 10000
        sa = sa + 1
        print sa
        print 'b'
    elif abs(x[0] - FluxT[x[0]]) > 1000:
        n = n / 1000
        sa = sa - 1
        print sa
        print 'c'
    elif abs(x[0] - FluxT[x[0]]) < 1000:
        n = n * 1000
        sa = sa + 1
        print sa
        print 'd'
    elif abs(x[0] - FluxT[x[0]]) > 100:
        n = n / 100
        sa = sa - 1
        print sa
        print 'd'
    elif abs(x[0] - FluxT[x[0]]) < 100:
        n = n * 100
        sa = sa + 1
        print sa
        print 'e'
    elif abs(x[0] - FluxT[x[0]]) > 10:
        n = n / 10
        sa = sa - 1
        print sa
        print 'f'
    elif abs(x[0] - FluxT[x[0]]) < 10:
        n = n * 10
        sa = sa + 1
        print sa
        print 'g'
    elif abs(x[0] - FluxT[x[0]]) > 1:
        n = n - 1
        sa = sa - 1
        print sa
        print 'h'
    elif abs(x[0] - FluxT[x[0]]) < 1:
        n = n + 1
        sa = sa + 1
        print sa
        print 'i'
    FluxT=FluxT/n

    

while x[0] != FluxT[x[0]]:
    if x[0] > FluxT[x[0]]:
        n = n - 10
        sa = sa - 1
        print sa
    if x[0] < FluxT[x[0]]:
        n = n + 10
        sa = sa + 1
        print sa
    FluxT=FluxT/n
    if abs(x[0] - FluxT[x[0]]) < 2:
        break
    

conv = 3.34e-57
a = max(FluxT)
b = plank(a, T)
n = conv*(b**2)
FluxF=FluxT/(n - 1)

"""


#bug test
print 4     

plt.plot(wavelengths*1e7, FluxT, 'r-') 
#plt.plot(wavelengths*1e7, FluxF, 'b-') 
plt.loglog(x,y,'b.')
plt.show()
plt.hold(True)

plt.xlim([1,1000])
plt.ylim([0.01,10])
#bug test
print 5

