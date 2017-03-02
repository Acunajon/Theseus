import numpy as np
import scipy
from scipy import stats
import astropy

sigma = np.array([1,6,3,8,6,4,2,7,54,7])
data = np.array([752,641,474,254,123,654,756,345,123,543])
Theorey = np.array([345,456,567,534,432,3345,867,123,543,567])

chi = lambda Theo, Dat, Sig: sum(((d-T)**2)/s**2)

print chi(Theorey, data, sigma)

def Re_chi2(b,c,a):
    """for i,j,k in zip(b,c,a):
        chi = sum(((i - j)**2)/(k**2))
    #c_d = DoF - FreP""" 
    pass
