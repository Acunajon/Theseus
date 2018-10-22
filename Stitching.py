"""
Stitching
"""
#normalizes IRS data to eachother

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


AllSources = getfiles('starfiles')
GoodStars =[]
BadStars = []
count = 0
for i in AllSources[0:10]:
    count += 1 
    print count
    insts = intlist(i)
    Source = tname(i)
    print Source
    if i == 'tests/.DS_Store':
        pass
    else:
        data = Table.read(i, format='ipac')
        plt.figure()
        plt.title('%s' %(Source))
        Her = []
        HerWave = []
        HerUn = []
        toMA = []
        toMAWave = []
        toMAUn = []
        WIS = []
        WISWave = []
        WISun = []
        SLone = []
        SLoneWave = []
        SLoneUN = []
        SLto = []
        SLtoWave = []
        SLtoUN = []
        LLone = []
        LLoneWave = []
        LLoneUN = []
        LLto = []
        LLtoWave = []
        LLtoUN = []
        for n in insts:
            for i in data:
                if n[len(n)-3:] == i['instrument'][len(i['instrument'])-3:]:
                    wave = i['wavelength']
                    flux = i['flux']
                    error = i['error']
                    if n[0:3] == 'Her':
                        HerWave.append(wave)
                        Her.append(flux)
                        HerUn.append(error)
                    if n[0:3] == '2MA':
                        toMAWave.append(wave)
                        toMA.append(flux)
                        toMAUn.append(error)
                    if n[0:3] == 'WIS':
                        WISWave.append(wave)
                        WIS.append(flux)
                        WISun.append(error)
                    if n == 'SpitzerIRS-SL1':
                        SLoneWave.append(wave)
                        SLone.append(flux)
                        SLoneUN.append(error)
                    if n == 'SpitzerIRS-SL2':
                        SLtoWave.append(wave)
                        SLto.append(flux)
                        SLtoUN.append(error)
                    if n == 'SpitzerIRS-LL1':
                        LLoneWave.append(wave)
                        LLone.append(flux)
                        LLoneUN.append(error)
                    if n == 'SpitzerIRS-LL2':
                        LLtoWave.append(wave)
                        LLto.append(flux)
                        LLtoUN.append(error)
        if len(SLone) > 0 or len(SLto) > 0 or len(LLone) > 0 or len(LLto) > 0:
            SLone = np.array(SLone)
            SLoneWave = np.array(SLoneWave)
            SLto = np.array(SLto)
            SLtoWave = np.array(SLtoWave)
            LLone = np.array(LLone)
            LLoneWave = np.array(LLoneWave)
            LLto = np.array(LLto)
            LLtoWave = np.array(LLtoWave)
            try:
                point1 = (LLoneWave[0] + LLtoWave[len(LLto)-1])/2
                ll_one_beg = np.interp(point1, LLoneWave, LLone)
                ll_to_end = np.interp(point1, LLtoWave, LLto)
                LLto *= ll_one_beg/ll_to_end
            except:
                pass
            try:
                point2 = (LLtoWave[0] + SLoneWave[len(SLone)-1])/2
                ll_to_beg = np.interp(point2, LLtoWave, LLto)
                sl_one_end = np.interp(point2, SLoneWave, SLone)
                SLone *= ll_to_beg/sl_one_end
            except:
                pass
            try:
                point3 = (SLoneWave[0] + SLtoWave[len(SLto)-1])/2
                sl_one_beg = np.interp(point3, SLoneWave, SLone)
                sl_to_end = np.interp(point3, SLtoWave, SLto)
                SLto *= sl_one_beg/sl_to_end
            except:
                pass



      
        
        if len(Her) > 1:
            plt.plot(HerWave, Her, '^', color='violet', label='Herschel')
            plt.errorbar(HerWave, Her,yerr=HerUn,linestyle="none")            
        else:
            pass
        if len(toMA) > 1:
            plt.plot(toMAWave, toMA, 'r*', label='2MASS')
            plt.errorbar(toMAWave, toMA,yerr=toMAUn,linestyle="none")
        else:
            pass
        if len(WIS) > 1:
            plt.loglog(WISWave, WIS, 'g*', label='WISE')
            plt.errorbar(WISWave, WIS, yerr=WISun,linestyle="none")
        else:
            pass
        if len(SLone) > 1:
            plt.plot(SLoneWave,SLone, 'y.', label='Spitzer-SL1')
            plt.errorbar(SLoneWave,SLone, yerr=SLoneUN,linestyle="none")
        else:
            pass
        if len(SLto) > 1:
            plt.loglog(SLtoWave, SLto, '.', color='orange', label='SpitzerIRS-SL2')
            plt.errorbar(SLtoWave, SLto, yerr=SLtoUN,linestyle="none")
        else:
            pass
        if len(LLone) > 1:
            plt.plot(LLoneWave, LLone, '.', color='indigo', label='SpitzerIRS-LL1')
            plt.errorbar(LLoneWave, LLone, yerr=LLoneUN,linestyle="none")
        else:
            pass
        if len(LLto) > 1:
            plt.plot(LLtoWave, LLto, 'b.', label='SpitzerIRS-LL2')
            plt.errorbar(LLtoWave, LLto, yerr=LLtoUN,linestyle="none")
        else:
            pass
        plt.legend(frameon=True) 
        try:
            plt.savefig('Results/%s' % (Source))
        except:
            print 'Could not store plot'

