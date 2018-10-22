"""
TEST FILE
"""

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
from scipy.stats import f
from scipy.stats import norm as Norm


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

starfiles = getfiles('Fomalhaut')                                                      #STARFILES AND THEIR WORK
GoodStars =[]
BadStars = []
count = 0       #set = to (first-1) in following for loop
for i in starfiles[1:2]:
    count += 1 
    print count
    if i == 'starfilesOrininal/.DS_Store':
        pass
    else:
        #FILE INPUT  DATA + NEXTGEN
        Source = tname(i)
        print Source
        insts = intlist(i)
        filein = Table.read('%s' % (i), format='ipac')
        DataWave = filein['wavelength']
        DataFlux = filein['flux']
        DataUncert = filein['error']
        #Tstar = tstar(i)
        #NextGen = ngfind(i)
        #NGwave, NGflux = data_ng('nextgen/%s' % (NextGen))

        data = Table.read(i, format='ipac')                                    #READS INDIVIDUAL STARFILE
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
        AllFlux = []
        AllWave = []
        AllEr = []
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
        if len(SLone) > 0:
            for i in SLone:
                AllFlux.append(i)
            for i in SLoneWave:
                AllWave.append(i)
            for i in SLoneUN:
                AllEr.append(i)
        if len(SLto) > 0:
            for i in SLto:
                AllFlux.append(i)
            for i in SLtoWave:
                AllWave.append(i)
            for i in SLtoUN:
                AllEr.append(i)
        if len(LLone) > 0:
            for i in LLone:
                AllFlux.append(i)
            for i in LLoneWave:
                AllWave.append(i)
            for i in LLoneUN:
                AllEr.append(i)
        if len(LLto) > 0:
            for i in LLto:
                AllFlux.append(i)
            for i in LLtoWave:
                AllWave.append(i)
            for i in LLtoUN:
                AllEr.append(i)
        if len(Her) > 0:
            HerSaturationLimits = [220, 510, 1125]
            HerschelWave = [70, 100,160]
            for i in HerWave:
                if i == 70:
                    a = HerWave.index(70)
                    b = Her[a]
                    c = HerWave[a]
                    d = HerUn[a]
                    e = HerSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 100:
                    a = HerWave.index(100)
                    b = Her[a]
                    c = HerWave[a]
                    d = HerUn[a]
                    e = HerSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 160:
                    a = HerWave.index(160)
                    b = Her[a]
                    c = HerWave[a]
                    d = HerUn[a]
                    e = HerSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                else:
                    pass
            #for i in Her:
             #   AllFlux.append(i)
            #for i in HerWave:
             #   AllWave.append(i)
            #for i in HerUn:
             #   AllEr.append(i)
        if len(toMA) > 0:
            toMASaturationLimits = [10.057, 10.24, 10.566]
            toMASSWave = [1.235, 1.662, 2.159]
            for i in toMAWave:
                if i == 1.235:
                    a = toMAWave.index(1.235)
                    b = toMA[a]
                    c = toMAWave[a]
                    d = toMAUn[a]
                    e = toMASaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 1.662:
                    a = toMAWave.index(1.662)
                    b = toMA[a]
                    c = toMAWave[a]
                    d = toMAUn[a]
                    e = toMASaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 2.159:
                    a = toMAWave.index(2.159)
                    b = toMA[a]
                    c = toMAWave[a]
                    d = toMAUn[a]
                    e = toMASaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                else:
                    pass
            #for i in toMA:
             #   AllFlux.append(i)
            #for i in toMAWave:
             #   AllWave.append(i)
            #for i in toMAUn:
             #   AllEr.append(i)
        if len(WIS) > 0:
            WiseSaturationLimits = [0.18, 0.36, 0.88, 12]
            WiseWave = [3.368, 4.618, 12.082, 22.194]
            for i in WISWave:
                if i == 3.368:
                    a = WISWave.index(3.368)
                    b = WIS[a]
                    c = WISWave[a]
                    d = WISun[a]
                    e = WiseSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 4.618:
                    a = WISWave.index(4.618)
                    b = WIS[a]
                    c = WISWave[a]
                    d = WISun[a]
                    e = WiseSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 12.082:
                    a = WISWave.index(12.082)
                    b = WIS[a]
                    c = WISWave[a]
                    d = WISun[a]
                    e = WiseSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                elif i == 22.194:
                    a = WISWave.index(22.194)
                    b = WIS[a]
                    c = WISWave[a]
                    d = WISun[a]
                    e = WiseSaturationLimits[a]
                    if b <= e:
                        AllFlux.append(b)
                        AllWave.append(c)
                        AllEr.append(d)
                else:
                    pass
            #for i in WIS:
             #   AllFlux.append(i)
            #for i in WISWave:
             #   AllWave.append(i)
            #for i in WISun:
             #   AllEr.append(i)



        WiseSaturationLimits = [0.18, 0.36, 0.88, 12]
        WiseWave = [3.368, 4.618, 12.082, 22.194]
        toMASaturationLimits = [10.057, 10.24, 10.566]
        toMASSWave = [1.235, 1.662, 2.159]
        HerSaturationLimits = [220, 510, 1125]
        HerschelWave = [70, 100,160]
        
        
        ########################BEGINNING PLOT##################################
        plt.figure()                                                           #BEGINNING PLOTS
        plt.title('%s' %(Source))            
        if len(Her) > 1:
            plt.plot(HerschelWave, HerSaturationLimits, '_', color='violet', label='Herschel')
            plt.plot(HerWave, Her, '^', color='violet', label='Herschel')
            plt.errorbar(HerWave, Her,yerr=HerUn,linestyle="none")            
        else:
            pass
        if len(toMA) > 1:
            plt.plot(toMASSWave, toMASaturationLimits, 'r_', label='Saturation Limit')
            plt.plot(toMAWave, toMA, 'r*', label='2MASS')
            plt.errorbar(toMAWave, toMA,yerr=toMAUn,linestyle="none")
        else:
            pass
        if len(WIS) > 1:
            plt.loglog(WiseWave, WiseSaturationLimits, 'g_', label='Saturation Limit')            
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
        #ylim = min(AllFlux)
        #if ylim < 0:
        #    ylim *= -1
        plt.plot(AllWave,AllFlux, '*', color='black', label='Used for Fitting')                                             #creates legend
        #plt.xlim(0.2*min(AllWave),1.5*max(AllWave))                                                                #locks x limits for plot
        #plt.ylim(1e-2*ylim,1.2*max(AllFlux))
        plt.ylabel(r'F$_\nu$ (Jy)')
        plt.xlabel(r'$\lambda$ ($\mu$m)')
        plt.legend(frameon=True) 
        plt.plot()
        plt.legend(frameon=True) 
        try:
            plt.savefig('Fomalhaut/%s' % (Source))
        except:
            print 'Could not store plot'
        plt.close



"""
bigN = 300.          # Number of data points
Nparam1 = 3.
Nparam2 = 5.
dof1 = bigN - Nparam1
dof2 = bigN - Nparam2

chi1 = 300. #428.65 #383.6 #really bad
chi2 = 300.  #results in chisqr close to 1

ftest = (chi1/(dof1)) / (chi2/(dof2))
           #RJ+BB vs RJ+BB+BB
#ftest = ( (chi1-chi2)/(dof1-dof2) ) / (chi2/dof2)

proba_at_f_pdf = f.pdf(ftest, dof1, dof2)
proba_at_f_cdf = f.cdf(ftest, dof1, dof2)           # P(F(1,30) < 3)
f_at_proba_98  = f.ppf(.98, dof1, dof2)             # q such P(F(1,30) < .95)
proba_at_norm_idf = norm.isf(proba_at_f_cdf)         # P(F(1,30) < 3)
proba_at_norm_ppf = norm.ppf(proba_at_f_cdf)         # P(F(1,30) < 3)

#if proba_at_f_cdf > .98 then choose 2BB, ignore 1BB






        plt.figure()                                                           #BEGINNING PLOTS
        plt.title('%s' %(Source))            
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
        plt.plot()
        plt.legend(frameon=True) 
        try:
            plt.savefig('Results/%s' % (Source))
        except:
            print 'Could not store plot'
"""

