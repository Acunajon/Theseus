"""
THIS IS A PLANCK FUNCTION FOR TWO SEPERATE SOURCES
"""

import math

"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)
k = 1.38064852*10**(-23)
c = 299792458   
"""CONSTANTS"""

def Planck_2(Wav, T, Norm, T_IN, Norm_IN):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_IN)
    Conv = ((Wav**2)/c)*10**-19
    Flux_IN = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_IN
    Flux_T = Flux + Flux_IN
    return Flux_T