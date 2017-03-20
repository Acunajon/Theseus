"""
JonathanAcuna
"""

from fitting import *
#fitting(wave, value, sigma, T_star, loop_num=1000):
from planck import *
#planck(Wav, T=100, Norm=1):
from preprocess import *
#data(directory) getfiles(directory)

import numpy as np
import matplotlib.pyplot as plt


Values = [['Norm', 'T_Disk_1', 'Norm_Disk_1', 'T_Disk_2', 'Norm_Disk_2', 'Chi']]
f = getfiles('batch_list')
for i in f:
    x, y, z = data(i)
    Norm, T_Disk_1, Norm_Disk_1, T_Disk_2, Norm_Disk_2, Chi = fitting(x, y, z, 8870, loop_num=1)
    i = []
    i.append(Norm)
    i.append(T_Disk_1)
    i.append(Norm_Disk_1)
    i.append(T_Disk_2)
    i.append(Norm_Disk_2)
    i.append(Chi)
    Values.append(i)