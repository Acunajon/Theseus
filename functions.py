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
    
#for opening a single columb file.
def data_1(f):
    d = np.genfromtxt(f, skip_header=1)
    x = []
    for i in d:
        x.append(i)
    return x
    
    
#to open files with more than one column seperated by | .  right now set to take first two columns.  ignores the rest.    
def data_2(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory as list of files
        contents = f.readlines()                            #stores all files in directory in a list
        for l in contents:                                  #opens and cycles list of files
            if 'name' not in l:                             #skips the header line   
                temp = l.split("|")                         #sorts each row by the | symbol in elemental arrays 
                c1 = temp[0].rstrip( )                      #strips spaces from right side of 1st column
                c2 = temp[1].rstrip( )                      #strips spaces from right side of 2nd column 
                c1 = c1.lstrip( )                           #strips spaces from left of 1st column 
                c2 = c2.lstrip( )                           #strips spaces from left side of 2nd column      
                arr.append([c1,c2])                         #apppends 1st and 2nd columns to arr array.   
    return arr                                              #returns an array of pairs.
            
#opens signal column data files and stores into array
def data_3(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory 
        contents = f.readlines()[0].split('\r')             #stores files from directory as list
        for l in contents:                                  #opens file
            if l.rstrip().lstrip() != 'name':               #skips header line 'name'
                arr.append(l.lstrip( ).rstrip( ))           #strips left and right side spaces and stores into array arr 
    return arr                                              #returns array arr
    
#opens single file and orginizes contents for analysis
def data(f):
    d = np.genfromtxt(f, skip_header=1)
    x = []
    y = []
    z = []
    for i in d:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return x, y, z
    
def data_ng(f):
    d = np.genfromtxt(f, skip_header=1)
    x = []
    y = []
    for i in d:
        x.append(i[0]*1.0e-4)
        y.append(i[1]*i[0]**2/c_cgs/1.0e8*1.0e23)
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

#to compare two lists and remove like values
def compare(a,b):
    A = []                                         #Empty list for later use                     
    B = []                                         #empty list for later use
    for i in a:                                    #cycles through first called list
        A.append(i)                                #appends each element of first called list to first empty list
    for i in b:                                    #cycles through second called list
        B.append(i)                                #appends each element of second called list to second emypty list
    check = 0                                      #starts a counter for loop
    while check < 10:                              #loop value at end
        check += 1                                 #increased counter value per loop 
        for i in A:                                #cycles through each element in first list IOT
            for n in B:                            #cycle each element in second list 
                if i == n:                         #compares the two elements for equality
                    A.remove(i)                    #removes element from list A if paired correctly with B
                    B.remove(n)                    #removes element from list B if paired correctly with B
                else:                              #if no pair is found 
                    pass                           #nothing happens 
    if len(A) > len(B):                            #checks for the longer list A or B 
        return A                                 
    else:                                          #returns the longer list
        return B
    
    
    
    
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