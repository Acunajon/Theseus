import math

"""CONSTANTS"""
pi = math.pi
e = math.e
h = 6.62607004*10**(-34)
k = 1.38064852*10**(-23)
c = 299792458   
"""CONSTANTS"""

def Planck_3(Wav = np.arange(1e-6, 500e-6, 1e-6), T, Norm, T_Inner, Norm_Inner, T_Outer, Norm_Outer):
    a = 2*h*c**2
    b = h*c/(Wav*k*T)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Star = (a/Wav**5)*(1/(e**(b)-1))*Conv*Norm
    b_IN = h*c/(Wav*k*T_Inner)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Inner = (a/Wav**5)*(1/(e**(b_IN)-1))*Conv*Norm_Inner
    b_OUT = h*c/(Wav*k*T_Outer)
    Conv = ((Wav**2)/c)*10**-19
    Flux_Outer = (a/Wav**5)*(1/(e**(b_OUT)-1))*Conv*Norm_Outer
    Flux_Tot = Flux_Star + Flux_Inner + Flux_Outer
    return Flux_Star, Flux_Inner, Flux_Outer, Flux_Tot