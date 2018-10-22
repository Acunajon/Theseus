"""
Jonathan Acuna
"""
from constants import *
import os
import numpy as np

#plannk function   output in (Jy)
def planck(Wav, T=100, Norm=1):
    from scipy.constants import h,k,c
    Flux = (( (2*h*c) / (Wav**3) ) * ( 1 / (np.exp(h*c/(Wav*k*T))-1) ) * (10**19)) * Norm
    return Flux

#pells the header info from a Ipac style data file
def header(i):
    header = []
    with open(i, 'r') as td:
        for line in td:
            # find the commented lines
            if line[0] == '\\':
                header.append(line)
    return header

#takes a datafile and returns a list of the instruments.
def intlist(fill):
    if fill == 'tests/.DS_Store':
        pass
    else:
        data = Table.read(fill, format='ipac')
        instlist = []
        for line in data:
            inst = line['instrument']
            if inst not in instlist:
                instlist.append(inst)
            else:
                pass
        return instlist

#pulls the star name out of the header info for a ipac style data file
def tname(i):
    header = []
    with open(i, 'r') as td:
        for line in td:
            # find the commented lines
            if line[0] == '\\':
                header.append(line)
    for i in header:
        if i[1:5] == 'NAME':
            mark = i.index('=')
            name = i[mark+1:].lstrip( ).rstrip('\n')
    return name

#pulls the temperature out of the header info for a ipac style data file
def tstar(i):
    header = []
    with open(i, 'r') as td:
        for line in td:
            # find the commented lines
            if line[0] == '\\':
                header.append(line)
    for i in header:
        if i[1:5] == 'TEMP':
            mark = i.index('=')
            temp = i[mark+1:].lstrip( ).rstrip('\n')
    return temp

#Pulls the spectral type out of the header
def SpcType(i):
    header = []
    with open(i, 'r') as td:
        for line in td:
            # find the commented lines
            if line[0] == '\\':
                header.append(line)
    for i in header:
        if i[1:5] == 'SpTy':
            mark = i.index('=')
            temp = i[mark+1:].lstrip( ).rstrip('\n')
    return temp    

#Pulls the star age out pf the header
def StrAge(i):
    header = []
    with open(i, 'r') as td:
        for line in td:
            # find the commented lines
            if line[0] == '\\':
                header.append(line)
    for i in header:
        if i[1:4] == 'AGE':
            mark = i.index('=')
            temp = i[mark+1:].lstrip( ).rstrip('\n')
    return temp

#normalizes blackbody curve to data
def normilize(x,y):
    from functions import planck
    one = planck(x[0], 100)
    norm = y[0]/one
    if norm < 0:
        norm *= -1
    return norm

#normalizes NextGen model to data
def norm_ng(x, y, X, Y):
    import numpy as np
    Ys = np.interp(x,X,Y)
    Yn = ((y[0])/(Ys[0]))
    if Yn < 0:
        Yn *= -1
    return Yn

#planck function for forword model
def bbl(lam, T):
    from scipy.constants import h,k,c
    import numpy as np
    lam = 1e-6 * lam
    return  (2*h*c**2 / (lam**5 * (np.exp(h*c/(lam*k*T)) - 1))) * (lam**2/c) * 1.0e19

#model function for Scipy.optimize.curve_fit
def forwardmodel(x, T1, T2, N1, N2, Ns):
    from functions import bbl
    return N1*bbl(x,T1) + N2*bbl(x,T2) + Ns*Ys

#fitting routine bundle
def optifit(wave,x,y,z,T):
    def bbl(lam, T):
        from scipy.constants import h,k,c
        import numpy as np
        lam = 1e-6 * lam
        return  (2*h*c**2 / (lam**5 * (np.exp(h*c/(lam*k*T)) - 1))) * (lam**2/c) * 1.0e19
    
    def forwardmodel(x, T1, T2, N1, N2, Ns):
        return N1*bbl(x,T1) + N2*bbl(x,T2) + Ns*bbl(x,T)
    
    from scipy.optimize import curve_fit
    popt, pcov = curve_fit(forwardmodel, x, y, p0=(100,100,1,1,1), sigma=z)
    return popt

#fitting routine bundle works with initial parameters matched
def optistar(Wav,x,y,z,T,Ys,popt7):
    def bbl(Wav, T):
        from scipy.constants import h,k,c
        import numpy as np
        Wav = 1e-6 * Wav
        return  (2*h*c**2 / (Wav**5 * (np.exp(h*c/(Wav*k*T)) - 1))) * (Wav**2/c) * 1.0e19
    
    def forwardmodel(x, T1, T2, N1, N2, Ns):
        return N1*bbl(x,T1) + N2*bbl(x,T2) + Ns*Ys
    
    from scipy.optimize import curve_fit
    count = 0
    while count < 10:
        count += 1
        popt, pcov = curve_fit(forwardmodel, x, y, p0=popt7, sigma=z)
        print popt[4]
        popt7 = popt
    print 'output order; T1, T2, N1, N2, Ns'
    return popt

#for opening a single columb file.
def data_1(f):
    import numpy as np
    d = np.genfromtxt(f, skip_header=1)
    x = []
    for i in d:
        x.append(i)
        print i
    x = np.array(x)
    return x
    
#to open files with more than one column seperated by | .  right now set to take first two columns.  ignores the rest.    
def data_2(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory as list of files
        contents = f.readlines()                            #stores all files in directory in a list
        for l in contents:                                  #opens and cycles list of files
            if 'name' not in l:                             #skips the header line   
                temp = l.split("\r")                         #sorts each row by the | symbol in elemental arrays 
                c1 = temp[0].rstrip( )                      #strips spaces from right side of 1st column
                c2 = temp[1].rstrip( )                      #strips spaces from right side of 2nd column 
                c1 = c1.lstrip( )                           #strips spaces from left of 1st column 
                c2 = c2.lstrip( )                           #strips spaces from left side of 2nd column      
                arr.append([c1,c2])                         #apppends 1st and 2nd columns to arr array.   
    return arr                                              #returns an array of pairs.
    

#to open files with more than one column seperated by | .  right now set to take first two columns.  ignores the rest.    
def data_12(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory as list of files
        contents = f.readlines()                            #stores all files in directory in a list
        for l in contents:                                  #opens and cycles list of files
            if 'name' not in l:                             #skips the header line   
                temp = l.split(" ")                         #sorts each row by the | symbol in elemental arrays 
                c1 = temp[0].rstrip( )                      #strips spaces from right side of 1st column
                c2 = temp[1].rstrip( )                      #strips spaces from right side of 2nd column 
                c1 = c1.lstrip( )                           #strips spaces from left of 1st column 
                c2 = c2.lstrip( )                           #strips spaces from left side of 2nd column      
                arr.append([c1,c2])                         #apppends 1st and 2nd columns to arr array.   
    return arr                                              #returns an array of pairs.

#to open files with more than one column seperated by | .  right now set to take first two columns.  ignores the rest.    
def data_34(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory as list of files
        contents = f.readlines()                            #stores all files in directory in a list
        for l in contents:                                  #opens and cycles list of files
            if 'name' not in l:                             #skips the header line   
                temp = l.split(" ")                         #sorts each row by the | symbol in elemental arrays 
                c3 = temp[0].rstrip( )                      #strips spaces from right side of 1st column
                c4 = temp[1].rstrip( )                      #strips spaces from right side of 2nd column 
                c3 = c3.lstrip( )                           #strips spaces from left of 1st column 
                c4 = c4.lstrip( )                           #strips spaces from left side of 2nd column      
                arr.append([c3,c4])                         #apppends 1st and 2nd columns to arr array.   
    return arr                                              #returns an array of pairs.

#to open files with more than one column seperated by | .  right now set to take first two columns.  ignores the rest.    
def data_56(fname):
    arr = []                                                #empty array for later use
    with open(fname, 'r') as f:                             #opens file directory as list of files
        contents = f.readlines()                            #stores all files in directory in a list
        for l in contents:                                  #opens and cycles list of files
            if 'name' not in l:                             #skips the header line   
                temp = l.split(" ")                         #sorts each row by the | symbol in elemental arrays 
                c5 = temp[0].rstrip( )                      #strips spaces from right side of 1st column
                c6 = temp[1].rstrip( )                      #strips spaces from right side of 2nd column 
                c5 = c5.lstrip( )                           #strips spaces from left of 1st column 
                c6 = c6.lstrip( )                           #strips spaces from left side of 2nd column      
                arr.append([c5,c6])                         #apppends 1st and 2nd columns to arr array.   
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
    import numpy as np
    d = np.genfromtxt(f, skip_header=1)
    x = []
    y = []
    z = []
    for i in d:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)    
    return x, y, z

#inputs a 5 column data file
def data_5(f):
    import numpy as np
    d = np.genfromtxt(f, skip_header=1)
    a = []
    b = []
    c = []
    d = []
    e = []    
    for i in d:
        a.append(i[0])
        b.append(i[1])
        c.append(i[2])
        d.append(i[1])
        e.append(i[2])                
    return a, b, c, d, e

#inputs a 5 column data file
def data_6(f):
    import numpy as np
    d = np.genfromtxt(f, skip_header=1)
    a = []
    b = []
    c = []
    d = []
    e = [] 
    f = []
    for i in d:
        a.append(i[0])
        b.append(i[1])
        c.append(i[2])
        d.append(i[3])
        e.append(i[4])
        f.append(i[5])  
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    e = np.array(e)
    f = np.array(f)              
    return a, b, c, d, e, f

    
#opens the NextGen star models for use
def data_PACS(f):
    import numpy as np
    d = np.genfromtxt(f, skip_header=2)
    x = []
    y = []
    for i in d:
        x.append(i[0])                                                         #converts to microns
        y.append(i[1])                                                         #converts to jankies
    x = np.array(x)
    y = np.array(y)            
    return x, y

#opens the NextGen star models for use
def data_MIPs(f):
    import numpy as np
    d = np.genfromtxt(f, skip_header=1)
    x = []
    y = []
    for i in d:
        x.append(i[0])                                                         #converts to microns
        y.append(i[1])                                                        #converts to jankies
    x = np.array(x)
    y = np.array(y)            
    return x, y


#opens the NextGen star models for use
def data_ng(f):
    import numpy as np
    c_cgs = 2.99792458e10 
    d = np.genfromtxt(f, skip_header=0)
    x = []
    y = []
    for i in d:
        x.append(i[0]*1.0e-4)                                                  #converts to microns
        y.append(i[1]*i[0]**2/c_cgs/1.0e8*1.0e23)                              #converts to jankies
    x = np.array(x)
    y = np.array(y)            
    return x, y

#opens directory and cycles through files    
def getfiles(directory):
    import os
    files = []
    for filename in os.listdir(directory):
        files.append(directory + '/' + filename)
    return files

#takes star temp and finds nearest temp for nextgen model    
def temper(base):
    temp = int(base)
    if (temp / 100) % 2 == 0:
        A = (temp/100) * 100
    else:
        A = (temp/100 +1) * 100
    return A

#takes star temp and finds nearest temp for nextgen model    
def temper2(base):
    temp = int(base)
    if (temp / 100) % 2 == 0:
        A = (temp/1000) * 1000
    else:
        A = (temp/1000 +1) * 1000
    return A

#takes star temp and finds nearest temp for nextgen model    
def TemperKurucz(base):
    temp = int(base)
    if (temp / 100) % 5 == 0:
        A = (temp/100) * 100
    else:
        A = int(5 * round(temp/5)) * 100
    return A

#takes star temp and finds nearest temp for nextgen model    
def TemperKurucz2(base):
    temp = int(base)
    if (temp / 100) % 10 == 0:
        A = (temp/1000) * 1000
    else:
        A = int(1000 * round(temp/1000)) * 1000
    return A

#uses the star temp to call a NextGen model file
def ngfind(i):
    from functions import tstar
    from functions import temper
    if type(i) != int:
        Tstar = tstar(i)
    elif type(i) == int:
        Tstar = i
    else:
        print 'Check Temperature for NG'
    ngtemp = temper(Tstar)
    title = 'xp00_'+str(ngtemp)+'g40.txt'
    return title

#uses the star temp to call a NextGen model file
def KuruczFind(i):
    from functions import tstar
    from functions import TemperKurucz
    if type(i) != int:
        Tstar = tstar(i)
    elif type(i) == int:
        Tstar = i
    else:
        print 'Check Temperature for NG'
    Kurucztemp = TemperKurucz(Tstar)
    title = 'kp00_'+str(Kurucztemp)+'g40.txt'
    return title

#takes a datafile and returns a list of the instruments.
def intlist(fill):
    from astropy.table import Table
    if fill == 'tests/.DS_Store':
        pass
    else:
        data = Table.read(fill, format='ipac')
        instlist = []
        for line in data:
            inst = line['instrument']
            if inst not in instlist:
                instlist.append(inst)
            else:
                pass
        return instlist
        
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
        print 'from first list'                                 
    else:                                          #returns the longer list
        return B
        print 'from second list'

#takes a string and replaces all \ slashes with / slashes.
#can alter directories written for windows.    
def slash(tStr):
    for i in range(len(tStr)):
        if tStr[i] == '\\':
            tStr = str(tStr[:i] + '/' + tStr[i+1:])
    return tStr
    
#to be used during polynomial fit to find the value of end points.
#test = np.polyfit(range, value, deg=10)
def line(test,x):
    return test[0]*x**10 + test[1]*x**9 +test[2]*x**8 + test[3]*x**7 + test[4]*x**6 + test[5]*x**5 +test[6]*x**4 +test[7]*x**3 +test[8]*x**2 +test[9]*x +test[10] + 1

    
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