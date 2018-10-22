"""
TEST FILE
"""

from astropy.table import Table
#from fitting import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
from nobelt import *
from onebelt import *
from twobelt import *
from scipy.stats import f
from scipy.stats import norm as Norm
from scipy.integrate import simps as INT


PlotSwitch = raw_input("generate plots, 'yes' or 'no'? ")

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

Convo = getfiles('convolution')
for i in Convo:
    if i == 'convolution/zMIPs.txt':
        #opens file and stores each line into a array||||||||BAD FORMAT
        data = []
        with open(i, 'rU') as td:
            for line in td:
                data.append(line)
        #takes data reformats for use.
        MIPS = []
        for i in range(len(data)):
            arr = []
            x = data[i].strip('\n').split(' ')
            for m in x:
                if m == '':
                    pass
                else:
                    arr.append(m)
            MIPS.append(arr)
        #lists to be filled with data
        MIPs24response = []
        MIPs24wave = []
        MIPs70response = []
        MIPs70wave = []
        MIPs160response = []
        MIPs160wave = []
        #stores data to lists from the reformated data MIPS skips header.
        for i in MIPS[1:]:
            if len(i) == 6:
                MIPs24response.append(i[1])
                MIPs24wave.append(i[0])
                MIPs70response.append(i[3])
                MIPs70wave.append(i[2])
                MIPs160response.append(i[5])
                MIPs160wave.append(i[4])    
            if len(i) == 4:
                MIPs24response.append(i[1])
                MIPs24wave.append(i[0])
                MIPs160response.append(i[3])
                MIPs160wave.append(i[2])
            if len(i) == 2:
                MIPs160response.append(i[1])
                MIPs160wave.append(i[0])
        #changes data lists to np array format        
        MIPs24wave = np.array(MIPs24wave).astype('float64')
        MIPs70wave = np.array(MIPs70wave).astype('float64')
        MIPs160wave = np.array(MIPs160wave).astype('float64')
        MIPs24response = np.array(MIPs24response).astype('float64')
        MIPs70response = np.array(MIPs70response).astype('float64')
        MIPs160response = np.array(MIPs160response).astype('float64') 

SingleSpectral = []
SingleTemp = []
DoubleSpectral = []
DoubleTemp = []

SingleAge = []
SingleAgeTemp = []
DoubleAge = []
DoubleAgeTemp = []
AgeList = []
AgeTempList = []


SingleSpitzer = 0
DoubleSpitzer = 0
TotalSpitzer = 0

WISCount = 0
#330 have WISE
AgeCount = 0
#129 have age

starfiles = getfiles('GoodStarfiles')   
DataTable1 = [['Star Name', 'Spectral Type', 'TStar', 'T Single', 'Reduced ChiSquare']]
DataTable2 = [['Star Name', 'Spectral Type', 'TStar', 'T Warm', 'T Cold', 'Reduced ChiSquare']]
TempList1BB = []
TempList2BB = []
TempListWarm = []
TempListCold = []
Stars1 = []
Stars2 = []
GoodStars =[]
BadStars = []
FitStars1 =[]
UnfitStars1 = []
FitStars2 =[]
UnfitStars2 = []
count = 0       #set = to (first-1) in following for loop
for i in starfiles[1:]:
    count += 1 
    print count
    try:
        if i == 'stars/.DS_Store':
            pass
        else:
            #FILE INPUT  DATA + NEXTGEN
            StarValue = 0
            DataList = []
            Source = tname(i)
            print Source
            DataList.append(Source)
            SpecTpe = SpcType(i)
            Age = StrAge(i)
            DataList.append(SpecTpe)
            insts = intlist(i)
            filein = Table.read('%s' % (i), format='ipac')
            DataWave = filein['wavelength']
            DataFlux = filein['flux']
            DataUncert = filein['error']
            Source = tname(i)
            Tstar = tstar(i)
            DataList.append(Tstar)
            NextGen = ngfind(i)
            StarWave, StarFlux = data_ng('nextgen/%s' % (NextGen))
            
            
            
            print Age, 'Age'
            if Age == 'nan':
                AgeCount += 1
                age = 'nan'
            elif Age != 'nan':
                age = int(Age.rstrip('0').rstrip('.')) 
                AgeList.append(age)
                AgeTempList.append(Tstar)
                print type(age)
            else:
                pass
            print age, 'age'
            
            if SpecTpe[0] == 'O':
                SpectralRef = 1 + (0.1*int(SpecTpe[1]))
            elif SpecTpe[0] == 'B':
                SpectralRef = 2 + (0.1*int(SpecTpe[1]))
            elif SpecTpe[0] == 'A':
                SpectralRef = 3 + (0.1*int(SpecTpe[1]))
            elif SpecTpe[0] == 'F':
                SpectralRef = 4 + (0.1*int(SpecTpe[1]))
            elif SpecTpe[0] == 'G':
                SpectralRef = 5 + (0.1*int(SpecTpe[1]))
            elif SpecTpe[0] == 'K':
                SpectralRef = 6 + (0.1*int(SpecTpe[1]))
            elif SpecTpe[0] == 'M':
                SpectralRef = 7 + (0.1*int(SpecTpe[1]))
            else:
                pass
            
            """
            if int(Tstar) < 10005:
                NextGen = ngfind(i)
                StarWave, StarFlux = data_ng('nextgen/%s' % (NextGen))
            elif int(Tstar) > 10005 and int(Tstar) < 13005:
                Kurucz = KuruczFind(i)
                StarWave, StarFlux = data_ng('Kurucz/%s' % (Kurucz))
            else:
                print 'Check Temp'
            """
            
            
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
            Spitzer = 'no'
            if len(SLone) > 0 or len(SLto) > 0 or len(LLone) > 0 or len(LLto) > 0:
                Spitzer = 'yes'
                TotalSpitzer += 1
                SLone = np.array(SLone)
                SLoneWave = np.array(SLoneWave)
                SLto = np.array(SLto)
                SLtoWave = np.array(SLtoWave)
                LLone = np.array(LLone)
                LLoneWave = np.array(LLoneWave)
                LLto = np.array(LLto)
                LLtoWave = np.array(LLtoWave)
                ###########STITCHING FOR IRS MODULES###############
                if len(LLone) > 0:
                    IRSFlux24=(INT(np.interp(MIPs24wave,LLoneWave,LLone)*MIPs24response,MIPs24wave))/INT(MIPs24response,MIPs24wave)
                    IRSFlux24NormValue = np.interp(24, LLoneWave, LLone)
                    LLone=LLone*(IRSFlux24/IRSFlux24NormValue)
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
                WISCount += 1
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
            ############### INSERT CODE FOR STAR LUMINOUSITY HERE  ############
            ############### INSERT CODE FOR STAR LUMINOUSITY HERE  ############

            
            #####################    ONE BELT DATA   ##############################

            DataWave1 = AllWave
            DataFlux1 = AllFlux
            DataUncert1 = AllEr
            
            #Variables
            wave = np.arange(1e-6, 500e-6, 1e-6)                                       #wave range in meters
            wavew = np.arange(1, 500, 1)                                               #wave range in microns
            NGfluxDataWave = np.interp(AllWave,StarWave,StarFlux)                                                          #interpolation of NextGen in data wave range
            Yw = np.interp(wavew,StarWave,StarFlux)                                        #interpolation of NextGen data in BlackBody wave range
            T1 = 137                                                                   #initlal temperature for inner belt
            num = 1
            
            #normalizer functions
            
            FluxNorm = norm_ng(AllWave,AllFlux,StarWave,StarFlux)                              #initial normalizer for NextGen values
            norm = normilize(AllWave,AllFlux)                                        #initial normalizers for blackdodies
            Yn = FluxNorm
            
        
            #this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
            def forwardmodel(AllWave, T1, N1, Ns):                                    #function used by curve_fit
                from functions import bbl
                return N1*bbl(AllWave,T1) + Ns*NGfluxDataWave
            
            try:    
                popt, pcov = curve_fit(forwardmodel, AllWave, AllFlux, p0=(100,norm,FluxNorm), sigma=AllEr) #find values for the fitting 
                uncert = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value
                FitStars1.append(Source)
            except:
                popt = [0, norm, FluxNorm]
                T1 = 0
                uncert = [1]
                print 'Error with 1BB Pre-Ftest'
                UnfitStars1.append(Source)
                BadStars.append(Source)
            
    
            #StarFlux *= popt[2]                                                                   #normalizes the NextGen values
            
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
            
            
            ######################      TWO BELT DATA      ########################
            DataWave2 = AllWave
            DataFlux2 = AllFlux
            DataUncert2 = AllEr
            
            
            #Variables
            wave = np.arange(1e-6, 500e-6, 1e-6)                                           #wave range in meters
            wavew = np.arange(1, 500, 1)                                                   #wave range in microns
            NGfluxDataWave = np.interp(DataWave2,StarWave,StarFlux)                                                          #interpolation of NextGen in data wave range
            Yw = np.interp(wavew,StarWave,StarFlux)                                                      #interpolation of NextGen data in BlackBody wave range
            T1 = 70                                                                       #initlal temperature for inner belt
            T2 = 255                                                                       #initial temperature for outer belt
            num = 2
            
            #normalizer functions
            FluxNorm = norm_ng(DataWave2,DataFlux2,StarWave,StarFlux)                                                          #initial normalizer for NextGen values
            norm = normilize(DataWave2,DataFlux2)                                                               #initial normalizers for blackdodies
            
            
            
            #this function needs access to NGfluxDataWave but not as an argument so has to be in this code.    
            def forwardmodelto(DataWave2, T1, T2, N1, N2, Ns):                                       #function used by curve_fit
                from functions import bbl
                return N1*bbl(DataWave2,T1) + N2*bbl(DataWave2,T2) + Ns*NGfluxDataWave
            try:     
                popt2, pcov = curve_fit(forwardmodelto, AllWave, AllFlux, p0=(200,80,norm,norm,FluxNorm), sigma=AllEr) #find values for the fitting 
                uncert2 = np.sqrt(np.diag(pcov))                                         #the uncertainties for each value
                FitStars2.append(Source)
            except:
                popt2 = [0, 0, norm, norm, FluxNorm]
                T1 = 0
                T2 = 0
                uncert = [1,1]
                print 'Error with 2BB pre-Ftest'
                UnfitStars2.append(Source)
                BadStars.append(Source)

            #StarFlux *= popt2[4]                                                                   #normalizes the NextGen values
            
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


            #print '-----------'
            if proba_at_f_cdf <= .98:
                print 'Source has a single belt.', 
                print 'Belt temperature is %i K' % (popt[0])
            else:
                print 'Source has two belts'
                print 'Warm belt temperature is %i K' % (popt2[0])
                print 'Cold belt temperature is %i K' % (popt2[1])
            #print '-----------'
            #print 'Source:         ', Source
            #print 'ftest:          ', ftest
            #print 'proba_at_f_pdf: ', proba_at_f_pdf
            #print 'proba_at_f_cdf: ', proba_at_f_cdf
            #print 'f_at_proba_98:  ', f_at_proba_98
            #print 'proba_at_norm_isf: ', proba_at_norm_idf      # inverse survival function
            #print 'proba_at_norm_ppf: ', proba_at_norm_ppf, ' sigma'  # Number of sigma away
            #print '-----------'
            #####################END OF FTEST SECTION##############################
    
            #print 'fitting'
            ################BEGINNING FIT FOR PLOTS AND STORAGE####################
            if proba_at_f_cdf <= .98 and len(popt) == 3 and popt[0] > 0 and popt[0] < 372:
                StarValue = 1
                Stars1.append(Source)

                SingleSpectral.append(SpectralRef)
                SingleTemp.append(int(Tstar))

                if Age != 'nan':
                    SingleAge.append(age)
                    SingleAgeTemp.append(int(Tstar))
                else:
                    pass

                if Spitzer == 'yes':
                    SingleSpitzer += 1

                TempList1BB.append(popt[0])
                Temperature = popt[0]
                DataList.append(format(Temperature, '.2f'))
                #DataList.append(popt[0])
                DataList.append(format(chisq1/dof1, '.2f'))
                StarFlux *= popt[2]                                                                   #normalizes the NextGen values
                #Main SED info
                inner = planck(wave, popt[0]) * popt[1]                                        #calls function for inner blackbody
                some = Yw*popt[2] + planck(wave, popt[0]) * popt[1]                                                  #creates the summation value array 
                #Excess info
                excess = DataFlux1 - NGfluxDataWave*popt[2]
                #inner see above
                #outer see above
                exsum = inner 
                #Residual info
                Yr = np.interp(DataWave1, wavew, some)
                res = (DataFlux1 - Yr) / DataUncert1
                zero = wavew * 0
                #Chi Calculator
                DoF1 = len(DataWave1)-3
                chi1 = (DataFlux1 - Yr)/DataUncert1
                chisq1 = np.dot(chi1, chi1)
                rechisq1 = chisq1 / DoF1

            elif proba_at_f_cdf > .98 and len(popt2) == 5 and popt2[0] > 0 and popt2[0] < 372 and popt2[1] < 372:
                StarValue = 2
                Stars2.append(Source)
                
                DoubleSpectral.append(SpectralRef)
                DoubleTemp.append(int(Tstar))

                if Age != 'nan':
                    DoubleAge.append(age)
                    DoubleAgeTemp.append(int(Tstar))
                else:
                    pass
                
                if Spitzer == 'yes':
                    DoubleSpitzer += 1
                
                TempList2BB.append(popt2[0])
                TempList2BB.append(popt2[1])
                TempListWarm.append(popt2[0])
                TempListCold.append(popt2[1])
                Temperature1 = popt2[0]
                Temperature2 = popt2[1]
                DataList.append(format(Temperature1, '.2f'))
                #DataList.append(popt2[0])
                DataList.append(format(Temperature2, '.2f'))
                #DataList.append(popt2[1])
                DataList.append(format(chisq2/dof2, '.2f'))
                StarFlux *= popt2[4]                                                                   #normalizes the NextGen values
                
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
                Yr = np.interp(DataWave2, wavew, some)
                res = (DataFlux2 - Yr) / DataUncert2
                zero = wavew * 0
                
                #Chi Calculator
                DoF2 = len(DataWave2)-5
                chi2 = (DataFlux2 - Yr)/DataUncert2
                chisq2 = np.dot(chi2, chi2)
                rechisq2 = chisq2 / DoF2

            else:
                BadStars.append(Source)
                print 'Problem with ftest on star', Source
                if proba_at_f_cdf > .98:
                    print '2BB fitting error'
                    print len(popt2), + 'numer of fitting values'
                elif proba_at_f_cdf <= .98:
                    print '1BB fitting error'
                    print len(popt), + 'numer of fitting values'
                else:
                    print 'unknown error with fitting portion'
            ######################RUNNING BB FIT PER FTEST END#####################
            
            if proba_at_f_cdf > .98:
                DataTable2.append(DataList)
            elif proba_at_f_cdf <= .98:
                DataTable1.append(DataList)
            else:
                pass

            print ' '
            print ' '

            if PlotSwitch == 'yes':
                
                #print 'plotting'
                #print StarValue
                ########################BEGINNING PLOT##################################
                WiseSaturationLimits = [0.18, 0.36, 0.88, 12]
                WiseWave = [3.368, 4.618, 12.082, 22.194]
                toMASaturationLimits = [10.057, 10.24, 10.566]
                toMASSWave = [1.235, 1.662, 2.159]
                HerSaturationLimits = [220, 510, 1125]
                HerschelWave = [70, 100,160]
        
                plt.show(False)
                plt.figure()                                                           #BEGINNING PLOTS
                plt.title('%s' %(Source))            
                if len(Her) > 1:
#                    plt.scatter(HerschelWave, HerSaturationLimits, '_', color='violet', label='Herschel')
                    plt.plot(HerschelWave, HerSaturationLimits,'_', color='violet')
                    plt.plot(HerWave, Her, '^', color='violet', label='Herschel')
                    plt.errorbar(HerWave, Her,yerr=HerUn,linestyle="none")            
                else:
                    pass
                if len(toMA) > 1:
                    plt.plot(toMASSWave, toMASaturationLimits, 'r_')
                    plt.plot(toMAWave, toMA, 'r*', label='2MASS')
                    plt.errorbar(toMAWave, toMA,yerr=toMAUn,linestyle="none")
                else:
                    pass
                if len(WIS) > 1:
                    plt.loglog(WiseWave, WiseSaturationLimits, 'g_')            
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
                if proba_at_f_cdf > .98:
                    ylim = min(DataFlux2)
                    if ylim < 0:
                        ylim *= -1
                    plt.loglog(StarWave,StarFlux, 'c:', label='NextGen')                                         #NextGen plot
                    plt.plot(DataWave2,DataFlux2,'k.',lw=0.1, label='IR Data')                                           #plots spectral data
                    plt.errorbar(DataWave2,DataFlux2,yerr=DataUncert2,linestyle="none")
                    plt.plot(wavew,some, 'y--', label='Best Fit')                                  #plots the summation
                    plt.plot(wavew,inner, 'r-', label='T=%3i$\pm$%1i' % (popt2[0],uncert2[0]))       #plots the inner belt
                    plt.plot(wavew,outer, 'b--', label='T=%3i$\pm$%1i' % (popt2[1],uncert2[1]))       #plots the outer belt
                    plt.ylabel(r'F$_\nu$ (Jy)')
                    plt.legend(frameon=True)                                                       #creates legend
                    plt.xlim(0.2*min(DataWave2),1.5*max(DataWave2))                                                                #locks x limits for plot
                    plt.ylim(1e-2*ylim,100*max(DataFlux2))
                else:
                    pass
                if proba_at_f_cdf <= .98:
                    ylim = min(DataFlux1)
                    if ylim < 0:
                        ylim *= -1
                    #plt.title('%s with reduced chi square of %3f' % (Source, rechisq))                                                        #title of plot
                    plt.loglog(StarWave,StarFlux, 'c:', label='NextGen')                                         #NextGen plot
                    plt.plot(DataWave1,DataFlux1, 'k.', label='IR Data')                                           #plots spectral data
                    plt.errorbar(DataWave1,DataFlux1,yerr=DataUncert1,linestyle="none")
                    plt.plot(wavew,some, 'y--', label='Best Fit')                                  #plots the summation
                    plt.plot(wavew,inner, 'r-', label='T=%3i$\pm$%1i' % (popt[0],uncert[0]))       #plots the inner belt
                    plt.ylabel(r'F$_\nu$ (Jy)')
                    plt.legend(frameon=True)                                                       #creates legend
                    plt.xlim(0.2*min(DataWave1),1.5*max(DataWave1))                                                                #locks x limits for plot
                    plt.ylim(1e-2*ylim,100*max(DataFlux1)) 
                else:
                    pass
                plt.legend(frameon=True) 
                if StarValue == 1:
                    plt.savefig('Results1/%s' % (Source), dpi=300)
                elif StarValue == 2:
                    plt.savefig('Results2/%s' % (Source), dpi=300)
                else:
                    plt.savefig('ResultsB/%s' % (Source), dpi=300)


            else:
                pass
    except:
        #Source = tname(i)
        #BadStars.append(Source)
        pass


#plt.hist(TempList1BB)
#plt.savefig('Results/Hist')
plt.figure()
plt.title('Ages')
plt.xlabel('Star Age (Myr)')
plt.ylabel('Star Temp (K)')
plt.plot(SingleAge, SingleAgeTemp, 'g.', label='SingleBeltSystem')
plt.plot(DoubleAge, DoubleAgeTemp, 'r.', label='DoubleBeltSystem')
plt.plot(4600, 6000, 'y.', label='Sol')
plt.legend(frameon=True,fontsize=9)
plt.savefig('HRplot', dpi=300)
plt.close


"""   THIS GENERATES THE DATA TABLES AND PLOTS
import os
with open('DataTable1.csv', 'w') as file:
    for i in DataTable1:
        file.write('%s' % (i) + os.linesep)
with open('DataTable2.csv', 'w') as file:
    for i in DataTable2:
        file.write('%s' % (i) + os.linesep)

plt.figure()
plt.title('Temperature Ranges')
plt.ylabel('Number of Belts')
plt.xlabel('Dust Temperature')
plt.hist(TempList1BB, color='r', alpha=.60, label='single')
plt.hist(TempListWarm,color='b', alpha=.60, label='WarmBelts')
plt.hist(TempListCold,color='g', alpha=.60, label='ColdBelts')
plt.legend(frameon=True,fontsize=10)
plt.savefig('Histogram', dpi=300)
plt.close
    
plt.figure()
plt.title('Densities')
plt.ylabel('Temperature')
plt.xlabel('Spectral Type')
plt.plot(SingleSpectral, SingleTemp, 'g.', label='SingleBeltSystem')
plt.plot(DoubleSpectral, DoubleTemp, 'r.', label='DoubleBeltSystem')
plt.plot(5.2, 6000, 'y.', label='Sol')
plt.legend(frameon=True,fontsize=9)
plt.savefig('HRplot', dpi=300)
plt.close
"""

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

