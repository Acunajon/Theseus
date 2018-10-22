"""
Respones
"""
#reads in and normalizes response functions for each bandpass filter


from functions import *
import numpy as np

Convo = getfiles('convolution')
for i in Convo:
    print i
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
        #renomalizes response arrays
        MIPs24responseExpanded = MIPs24response / max(MIPs24response)
        MIPs70responseExpanded = MIPs70response / max(MIPs70response)
        MIPs160responseExpanded = MIPs160response / max(MIPs160response)
    if i == 'convolution/PacsFilter_blue.txt':
        PACSb_wave, PACSb_response = data_PACS(i)
        PACSb_response = PACSb_response / max(PACSb_response)
    if i == 'convolution/PacsFilter_green.txt':
        PACSg_wave, PACSg_response = data_PACS(i)
        PACSg_response = PACSg_response / max(PACSg_response)
    if i == 'convolution/PacsFilter_red.txt':
        PACSr_wave, PACSr_response = data_PACS(i)
        PACSr_response = PACSr_response / max(PACSr_response)
    elif i == 'convolution/RSR-W1.txt':
        WISE3wave, WISE3_response, WISE3un = data(i)
        WISE3_response = WISE3_response / max(WISE3_response)
    elif i == 'convolution/RSR-W2.txt':
        WISE4wave, WISE4_response, WISE4un = data(i)  
        WISE4_response = WISE4_response / max(WISE4_response)
    elif i == 'convolution/RSR-W3.txt':
        WISE12wave, WISE12_response, WISE12un = data(i) 
        WISE12_response = WISE12_response / max(WISE12_response)
    elif i == 'convolution/RSR-W4.txt':
        WISE22wave, WISE22_response, WISE22un = data(i)
        WISE22_response = WISE22_response / max(WISE22_response)
    else:
        pass
  
    
    
