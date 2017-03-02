"""TEST"""

Datx = [500,455,654,546,564]
Theoy = [250,243,243,265,276]
Uncz = [10,6,7,7,9,6]

"""GOAL: ROUTINE TO FOCUS THEOy TO DATx"""

def Re_Chi_2(Dat, Theo, Uncert, DoF=2, Para=1):
    
    Chi = 0
    for i in range(len(Dat)):
        Chi += ((Dat[i] - Theo[i])**2)/(Uncert[i]**2)
    return Chi/(DoF - Para)
