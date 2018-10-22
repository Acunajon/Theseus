"""
Histogram
"""
import numpy as np
import matplotlib.pyplot as plt

def data_Hist(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory 
        contents = f.readlines()
        for l in contents:                                  #opens file
            NewArray = []
            temp = l.split(",")
            if len(temp) == 9:
                TS = temp[4].lstrip( ).rstrip( )
                NewArray.append(TS)
                TW = temp[5].lstrip( ).rstrip( )
                NewArray.append(TW)
                TC = temp[6].lstrip( ).rstrip( )
                NewArray.append(TC)
                arr.append(NewArray)           #strips left and right side spaces and stores into array arr 
            else:
                pass
    return arr                                              #returns array arr

line = data_Hist('DataTablePrime.csv')
TSingle = []
TWarm = []
TCold = []
for i in line[1:]:
    if i[0] != "'nan'":
        a = i[0]
        try:
            b = float(a)
            c = int(b)
            if c > 0 and  c < 500:
                TSingle.append(c)
        except:
            pass
    if i[1] != "'nan'":
        a = i[1]
        try:
            b = float(a)
            c = int(b)
            if c > 0 and c < 500:
                TWarm.append(c)
        except:
            pass
    if i[2] != "'nan'":
        a = i[2]
        try:
            b = float(a)
            c = int(b)
            if c > 0 and c < 500:
                TCold.append(c)
        except:
            pass
    else:
        print type(float(i[1]))
        print float(i[1])
    
#plt.hist(TWarm, bins='auto')

plt.hist([TSingle, TWarm, TCold])







