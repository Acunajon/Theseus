"""
@author: JonathanAcuna
"""


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
print d


x = []
y = []
for i in d:
    x.append(i[0])
    y.append(i[1])
    
    
plt.loglog(x,y,'b.')
plt.show()


"""
np.log is ln, whereas np.log10 is your standard base 10 log.
plt.loglog   plots with axis in log vs log.
"""