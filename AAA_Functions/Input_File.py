"""
Jonathan Acuna >>>  Acunajon@Gmail.com

Read IN Function
"""

import numpy as np

def Input_File(File):
    with open(File, 'r') as sample1:
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
    return x, y, z
    
