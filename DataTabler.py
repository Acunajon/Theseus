"""
Data Table
"""

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

starfiles = getfiles('GoodStarfiles')   
DataTable = [['Star Name', 'Spectral Type', 'TStar', 'LStar', 'T Single', 'T Warm', 'T Cold', 'ReChi2', 'Age']]
TempList1BB = []
TempList2BB = []
GoodStars =[]
BadStars = []
count = 0       #set = to (first-1) in following for loop
for i in starfiles[1:]:
    count += 1 
    print count
    try:
        if i == 'stars/.DS_Store':
            pass
        else:
            #FILE INPUT  DATA + NEXTGEN
            DataList = []
            Source = tname(i)
            print Source
            DataList.append(Source)
            SpecTpe = SpcType(i)
            DataList.append(SpecTpe)
            StarAge = StrAge(i)
            insts = intlist(i)
            filein = Table.read('%s' % (i), format='ipac')
            DataWave = filein['wavelength']
            DataFlux = filein['flux']
            DataUncert = filein['error']
            Source = tname(i)
            Tstar = tstar(i)
            DataList.append(Tstar)
            NextGen = ngfind(i)
            NGwave, NGflux = data_ng('nextgen/%s' % (NextGen))
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
                            if source == 'HD 33262':
                                pass
                            else:
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
                ###########STITCHING FOR IRS MODULES###############
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
                #############RECOMBINATION OF DATA################
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
            #print 'Luminousity'
            ############### INSERT CODE FOR STAR LUMINOUSITY HERE  ############
            ############### INSERT CODE FOR STAR LUMINOUSITY HERE  ############
            #DataList.append(StarLum)
            DataList.append('nan')
            ############### INSERT CODE FOR STAR LUMINOUSITY HERE  ############
            ############### INSERT CODE FOR STAR LUMINOUSITY HERE  ############

            
            print 'Lists done'
            print '1B test'
            #####################    ONE BELT DATA   ##############################
            #DataWave1 = AllWave
            #DataFlux1 = AllFlux
            #DataUncert1 = AllEr
            
            #Variables
            wave = np.arange(1e-6, 500e-6, 1e-6)                                       #wave range in meters
            wavew = np.arange(1, 500, 1)                                               #wave range in microns
            NGfluxDataWave = np.interp(AllWave,NGwave,NGflux)                                                          #interpolation of NextGen in data wave range
            Yw = np.interp(wavew,NGwave,NGflux)                                        #interpolation of NextGen data in BlackBody wave range
            T1 = 100                                                                   #initlal temperature for inner belt
            num = 1
            
            #normalizer functions
            
            FluxNorm = norm_ng(AllWave,AllFlux,NGwave,NGflux)                              #initial normalizer for NextGen values
            norm = normilize(AllWave,AllFlux)                                        #initial normalizers for blackdodies
            Yn = FluxNorm
            
        
            #this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
            def forwardmodel(AllWave, T1, N1, Ns):                                    #function used by curve_fit
                from functions import bbl
                return N1*bbl(AllWave,T1) + Ns*NGfluxDataWave
            
            try:    
                popt, pcov = curve_fit(forwardmodel, AllWave, AllFlux, p0=(100,norm,FluxNorm), sigma=AllEr) #find values for the fitting 
                uncert = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value
            except:
                pass
                #popt = [100, norm, FluxNorm]
                #uncert = [1]
                #print 'Error with 1BB Pre-Ftest'
                #Source = Source + ' with unfit parameters'
            
    
            NGflux *= popt[2]                                                                   #normalizes the NextGen values
            
            #Main SED info
            inner = planck(wave, popt[0]) * popt[1]                                        #calls function for inner blackbody
            some = Yw*popt[2] + planck(wave, popt[0]) * popt[1]                                                  #creates the summation value array 
            
            #Excess info
            excess = AllFlux - NGfluxDataWave*popt[2]
            #inner see above
            #outer see above
            exsum = inner 
            
            #Residual info
            Yr = np.interp(AllWave, wavew, some)
            res = (AllFlux - Yr) / AllEr
            zero = wavew * 0
            
            #Chi Calculator
            DoF1 = len(AllWave)-3
            chi1 = (AllFlux - Yr)/AllEr
            chisq1 = np.dot(chi1, chi1)
            rechisq1 = chisq1 / DoF1
            ######################     END OF ONE BELT      #######################
            
            
            print '2B test'
            ######################      TWO BELT DATA      ########################
            DataWave2 = AllWave
            DataFlux2 = AllFlux
            DataUncert2 = AllEr
            
            
            #Variables
            wave = np.arange(1e-6, 500e-6, 1e-6)                                           #wave range in meters
            wavew = np.arange(1, 500, 1)                                                   #wave range in microns
            NGfluxDataWave = np.interp(DataWave2,NGwave,NGflux)                                                          #interpolation of NextGen in data wave range
            Yw = np.interp(wavew,NGwave,NGflux)                                                      #interpolation of NextGen data in BlackBody wave range
            T1 = 100                                                                       #initlal temperature for inner belt
            T2 = 100                                                                       #initial temperature for outer belt
            num = 2
            
            #normalizer functions
            FluxNorm = norm_ng(DataWave2,DataFlux2,NGwave,NGflux)                                                          #initial normalizer for NextGen values
            norm = normilize(DataWave2,DataFlux2)                                                               #initial normalizers for blackdodies
            
            
            
            #this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
            def forwardmodelto(DataWave2, T1, T2, N1, N2, Ns):                                       #function used by curve_fit
                from functions import bbl
                return N1*bbl(DataWave2,T1) + N2*bbl(DataWave2,T2) + Ns*NGfluxDataWave
            try:     
                popt2, pcov = curve_fit(forwardmodelto, AllWave, AllFlux, p0=(100,100,norm,norm,FluxNorm), sigma=AllEr) #find values for the fitting 
                uncert2 = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value
            except:
                pass
                #popt = [150, 60, norm, norm, FluxNorm]
                #uncert = [1,1]
                #print 'Error with 2BB pre-Ftest'
                #Source = Source + ' with unfit parameters and'
            
            NGflux *= popt2[4]                                                                   #normalizes the NextGen values
            
            #Main SED info
            inner = planck(wave, popt2[0]) * popt2[2]                                        #calls function for inner blackbody
            outer = planck(wave, popt2[1]) * popt2[3]                                        #calls function for outer blackbody
            some = Yw*popt2[4] + planck(wave,popt2[0],popt2[2]) + planck(wave,popt2[1],popt2[3])#creates the summation value array 
            
            #Excess info
            excess = DataFlux2 - NGfluxDataWave*popt2[4]
            #inner see above
            #outer see above
            exsum = inner + outer
            
            #Residual info
            Yr = np.interp(DataWave2, wavew, some)
            res = (DataFlux2 - Yr) / DataUncert2
            zero = wavew * 0
            
            #Chi Calculator
            DoF2 = len(DataWave2)-5
            chi2 = (DataFlux2 - Yr)/DataUncert2
            chisq2 = np.dot(chi2, chi2)
            rechisq2 = chisq2 / DoF2    
            #####################   END OF TWO BELT DATA   ########################
            
            
            print 'Ftest'
            ##########################    F-TEST    ###############################
            bigN = len(AllWave)          # Number of data points
            Nparam1 = 3.
            Nparam2 = 5.
            dof1 = bigN - Nparam1
            dof2 = bigN - Nparam2
            
            #chi1 = 300. #428.65 #383.6 #really bad
            #chi2 = 300.  #results in chisqr close to 1
            
            ftest = (chisq1/(dof1)) / (chisq2/(dof2))
                       #RJ+BB vs RJ+BB+BB
            #ftest = ( (chi1-chi2)/(dof1-dof2) ) / (chi2/dof2)
            
            proba_at_f_pdf = f.pdf(ftest, dof1, dof2)
            proba_at_f_cdf = f.cdf(ftest, dof1, dof2)           # P(F(1,30) < 3)
            f_at_proba_98  = f.ppf(.98, dof1, dof2)             # q such P(F(1,30) < .95)
            proba_at_norm_idf = Norm.isf(proba_at_f_cdf)         # P(F(1,30) < 3)
            proba_at_norm_ppf = Norm.ppf(proba_at_f_cdf)         # P(F(1,30) < 3)
    
            #####################END OF FTEST SECTION##############################
    
            print 'fitting'
            ################BEGINNING FIT FOR PLOTS AND STORAGE####################
            if f_at_proba_98 > 1:
                DataList.append('nan')
                
                TempList2BB.append(popt2[0])
                TempList2BB.append(popt2[1])
                DataList.append(popt2[0])
                DataList.append(popt2[1])
                NGflux *= popt2[4]                                                                   #normalizes the NextGen values
                
                #Main SED info
                inner = planck(wave, popt2[0]) * popt2[2]                                        #calls function for inner blackbody
                outer = planck(wave, popt2[1]) * popt2[3]                                        #calls function for outer blackbody
                some = Yw*popt2[4] + planck(wave,popt2[0],popt2[2]) + planck(wave,popt2[1],popt2[3])#creates the summation value array 
                
                #Excess info
                excess = AllFlux - NGfluxDataWave*popt2[4]
                #inner see above
                #outer see above
                exsum = inner + outer
                
                #Residual info
                Yr = np.interp(AllWave, wavew, some)
                res = (AllFlux - Yr) / AllEr
                zero = wavew * 0
                
                #Chi Calculator
                DoF2 = len(AllWave)-5
                chi2 = (AllFlux - Yr)/AllEr
                chisq2 = np.dot(chi2, chi2)
                rechisq2 = chisq2 / DoF2
                print rechisq2
                DataList.append(rechisq2)
                print 'test point'
            elif f_at_proba_98 <= 1:

                TempList1BB.append(popt[0])
                DataList.append(popt[0])
                DataList.append('nan')
                DataList.append('nan')
                NGflux *= popt[2]                                                                   #normalizes the NextGen values
                #Main SED info
                inner = planck(wave, popt[0]) * popt[1]                                        #calls function for inner blackbody
                some = Yw*popt[2] + planck(wave, popt[0]) * popt[1]                                                  #creates the summation value array 
                #Excess info
                excess = DataFlux1 - NGfluxDataWave*popt[2]
                #inner see above
                #outer see above
                exsum = inner 
                #Residual info
                Yr = np.interp(AllWave, wavew, some)
                res = (AllFlux - Yr) / AllEr
                zero = wavew * 0
                #Chi Calculator
                DoF1 = len(AllWave)-3
                chi1 = (AllFlux - Yr)/AllEr
                chisq1 = np.dot(chi1, chi1)
                rechisq1 = chisq1 / DoF1
                DataList.append(rechisq1)
            else:
                print 'Problem witih ftest on star', Source
                if f_at_proba_98 > 1:
                    print f_at_proba_98
                    print '2BB fitting error'
                    print len(popt2), + 'numer of fitting values'
                elif f_at_proba_98 <= 1:
                    print f_at_proba_98
                    print '1BB fitting error'
                    print len(popt), + 'numer of fitting values'
                else:
                    print 'unknown error with fitting portion'
            ######################RUNNING BB FIT PER FTEST END#####################
            try:
                DataList.append(StarAge)
            except:
                print 'Error finding Star Age'
            DataTable.append(DataList)
    except:
        #Source = tname(i)
        #BadStars.append(Source)
        pass




import os
with open('DataTable.csv', 'w') as file:
    for i in DataTable:
        file.write('%s' % (i) + os.linesep)


    
