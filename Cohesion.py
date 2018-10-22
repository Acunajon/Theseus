"""
Data Cohesion
"""
#reads in data and breals according to instrument

from astropy.table import Table
from fitting import *
from functions import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
from nobelt import *
from onebelt import *
from twobelt import *

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

f = getfiles('starfiles')
GoodStars =[]
BadStars = []
count = 0
for i in f:
    count += 1 
    print count
    insts = intlist(i)
    Source = tname(i)
    if i == 'tests/.DS_Store':
        pass
    else:
        data = Table.read(i, format='ipac')
        plt.figure()
        plt.title('%s' %(Source))           
        #following is the plot work.
        Her = []
        HerWave = []
        toMA = []
        toMAWave = []
        WIS = []
        WISWave = []
        SLone = []
        SLoneWave = []
        SLto = []
        SLtoWave = []
        LLone = []
        LLoneWave = []
        LLto = []
        LLtoWave = []
        for n in insts:
            for i in data:
                if n[len(n)-3:] == i['instrument'][len(i['instrument'])-3:]:
                    wave = i['wavelength']
                    flux = i['flux']
                    if n[0:3] == 'Her':
                        HerWave.append(wave)
                        Her.append(flux)
                    if n[0:3] == '2MA':
                        toMAWave.append(wave)
                        toMA.append(flux)
                    if n[0:3] == 'WIS':
                        WISWave.append(wave)
                        WIS.append(flux)
                    if n == 'SpitzerIRS-SL1':
                        SLoneWave.append(wave)
                        SLone.append(flux)
                    if n == 'SpitzerIRS-SL2':
                        SLtoWave.append(wave)
                        SLto.append(flux)
                    if n == 'SpitzerIRS-LL1':
                        LLoneWave.append(wave)
                        LLone.append(flux)
                    if n == 'SpitzerIRS-LL2':
                        LLtoWave.append(wave)
                        LLto.append(flux)
        if len(Her) > 1:
            plt.plot(HerWave, Her, '^', color='violet', label='Herschel')
        else:
            pass
        if len(toMA) > 1:
            plt.plot(toMAWave, toMA, 'r*', label='2MASS')
        else:
            pass
        if len(WIS) > 1:
            plt.loglog(WISWave, WIS, 'g*', label='WISE')
        else:
            pass
        if len(SLone) > 1:
            plt.plot(SLoneWave,SLone, 'y.', label='Spitzer-SL1')
        else:
            pass
        if len(SLto) > 1:
            plt.loglog(SLtoWave, SLto, '.', color='orange', label='SpitzerIRS-SL2')
        else:
            pass
        if len(LLone) > 1:
            plt.plot(LLoneWave, LLone, '.', color='indigo', label='SpitzerIRS-LL1')
        else:
            pass
        if len(LLto) > 1:
            plt.plot(LLtoWave, LLto, 'b.', label='SpitzerIRS-LL2')
        else:
            pass
        plt.legend(frameon=True) 
        try:
            plt.savefig('Results/%s' % (Source))
        except:
            print 'Could not store plot'