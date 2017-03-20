"""
Jonathan Acuna
"""
import os
import numpy as np

def data(f):
    sample1 = open(f, 'r')
    d = np.genfromtxt(f, skip_header=1)
    """s1=sample1.readlines()
    s1 = np.array(map(lambda x: x.strip(), s1))
    d = np.array(map(lambda x: x.split(), s1))#.reshape((-1,3))
    d = np.delete(d, [0,1,2]).reshape((-1,3))
    d = d.astype(float)"""
    x = []
    y = []
    z = []
    for i in d:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return x, y, z

def getfiles(directory):
    files = []
    for filename in os.listdir(directory):
        #x, y, z = data(directory + '\\' + filename)
        files.append(directory + '\\' + filename)
    return files

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