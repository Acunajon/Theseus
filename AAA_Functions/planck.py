"""
JonathanAcuna  

Planck function
"""



import math
import numpy as np


"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)
k = 1.38064852*10**(-23)
c = 299792458   
"""CONSTANTS"""


"""PLANK FUNCTION"""
def plank(Wav, T):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)+1))*Conv
    return Flux
"""PLANK FUNCTION END"""


"""WAVE LENGTH RANGE"""
wave = np.arange(1e-9, 500e-6, 1e-6) 
"""WAVE LENGTH RANGE"""

"""You can feed the function one wavelegth and temperature pair or a
range of either."""










"""
np.log is ln, whereas np.log10 is your standard base 10 log.
plt.loglog   plots with axis in log vs log.
"""