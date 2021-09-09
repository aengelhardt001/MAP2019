import numpy as np
import pynbody
import matplotlib as mpl
import pynbody.plot as pp
import pickle
import pandas as pd
import pynbody.plot.sph as sph
pynbody.config['halo-class-priority'] =  [pynbody.halo.ahf.AHFCatalogue,
                                          pynbody.halo.GrpCatalogue,
                                          pynbody.halo.AmigaGrpCatalogue,
                                          pynbody.halo.legacy.RockstarIntermediateCatalogue,
                                          pynbody.halo.rockstar.RockstarCatalogue,
                                          pynbody.halo.subfind.SubfindCatalogue,
                                          pynbody.halo.hop.HOPCatalogue]
sim1 = '/home/akinshol/Data/DataFiles/h148'
sim2 = '/home/akinshol/Data/DataFiles/h229'
sim3 = '/home/akinshol/Data/DataFiles/h242'
sim4 = '/home/akinshol/Data/DataFiles/h329'
CM = '/home/akinshol/Data/DataFiles/cptmarvel'
E = '/home/akinshol/Data/DataFiles/elektra'
R = '/home/akinshol/Data/DataFiles/rogue'
S = '/home/akinshol/Data/DataFiles/storm'

# here is where we will put whatever halo numbers we decide are interesting and worth computing
# i.e. all the halos with stars in them

nums1 = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 20, 21, 22, 23, 26, 27, 28, 30, 31, 32, 34, 36, 37, 38, 40, 41, 42, 45, 46, 48, 55, 57, 58, 60, 64, 71, 73, 77, 80, 91, 94, 95, 99, 106, 115, 121, 125, 126, 131, 140, 143, 160, 223, 252, 264, 271, 304, 353, 372, 373, 435, 465, 590, 647, 677, 682, 738, 869, 961, 980, 1146, 1155, 1381, 2792, 4897, 10814]
nums2 = [1, 2, 3, 4, 7, 14, 16, 17, 18, 19, 21, 22, 25, 27, 28, 29, 30, 33, 36, 41, 50, 51, 52, 56, 60, 62, 70, 73, 75, 95, 104, 108, 134, 203, 277, 553, 982, 1319, 1409, 1481, 4380, 5722]
nums3 = [1, 4, 9, 10, 11, 12, 19, 24, 29, 30, 33, 36, 39, 40, 45, 46, 48, 53, 57, 62, 66, 69, 70, 72, 75, 76, 85, 89, 102, 133, 152, 185, 211, 302, 425, 457, 536, 1773, 2748, 2891, 9059, 9126, 10085, 11901]
nums4 = [1, 8, 9, 13, 14, 19, 25, 31, 32, 40, 47, 63, 92, 99, 126, 129, 135, 170, 195, 444, 686, 942, 1418]

data1 = []

with open(sim1 + '.data', 'rb') as f:
    while True:
        try:
            data1.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    data1 = pd.DataFrame(data1)
data1['sim'] = ['h148']*len(data1)
    
    
data2 = []
    
with open(sim2 + '.data', 'rb') as f:
    while True:
        try:
            data2.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    data2 = pd.DataFrame(data2)
data2['sim'] = ['h229']*len(data2)    
    
data3 = []
    
with open(sim3 + '.data', 'rb') as f:
    while True:
        try:
            data3.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    data3 = pd.DataFrame(data3)
data3['sim'] = ['h242']*len(data3)    
    
data4 = []
    
with open(sim4 + '.data', 'rb') as f:
    while True:
        try:
            data4.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    data4 = pd.DataFrame(data4)
data4['sim'] = ['h329']*len(data4)
    
Cap_Marvel = []
    
with open(CM + '.data', 'rb') as f:
    while True:
        try:
            Cap_Marvel.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    Cap_Marvel = pd.DataFrame(Cap_Marvel)
Cap_Marvel['sim'] = ['cptmarvel']*len(Cap_Marvel)
    
Elektra = []
    
with open(E + '.data', 'rb') as f:
    while True:
        try:
            Elektra.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    Elektra = pd.DataFrame(Elektra)
Elektra['sim'] = ['elektra']*len(Elektra)
    
Rogue = []
    
with open(R + '.data', 'rb') as f:
    while True:
        try:
            Rogue.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    Rogue = pd.DataFrame(Rogue)
Rogue['sim'] = ['rogue']*len(Rogue)
    
Storm = []
    
with open(S + '.data', 'rb') as f:
    while True:
        try:
            Storm.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    Storm = pd.DataFrame(Storm)
Storm['sim'] = ['storm']*len(Storm)
    
MW = data1.append(data2)
MW = MW.append(data3)
MW = MW.append(data4)

data = data1.append(data2)
data = data.append(data3)
data = data.append(data4)
data = data.append(Cap_Marvel)
data = data.append(Elektra)
data = data.append(Storm)
data = data.append(Rogue)




S_nums1 = [2, 3, 5, 6, 9, 11, 12, 14, 26, 28, 31, 38, 42, 46, 60, 64, 77, 80, 125, 131, 223, 252, 264, 271, 304, 353, 
           372, 373, 435, 465, 590, 647, 682, 869, 961, 980, 1146, 1155, 1381, 2792, 4897]
S_nums2 = [21, 22, 27, 33, 50, 51, 52, 60, 70, 95, 104, 203, 277, 553, 982, 1409, 1481, 5722]
S_nums3 = [4, 10, 21, 27, 48, 71, 102, 131, 418, 1534, 9724, 11563]
S_nums4 = [11]
S_nums5 = [167, 455, 1328]
S_nums6 = [1, 2, 3, 4, 5, 8, 9, 10, 12, 18, 37]
S_nums7 = [36, 702, 848, 3626, 6092]
S_nums8 = [35, 43, 47, 60, 109, 125, 169, 218, 253, 292, 2423, 3127, 3738, 5779]

F_nums1 = [1, 10, 18, 23, 30, 34, 36, 55, 57, 94, 99, 115, 126, 160, 677, 738]
F_nums2 = [1, 2, 4, 9, 14, 16, 17, 29, 56, 62, 134, 1319]
F_nums3 = [1, 31, 35, 37, 45, 47, 49, 67, 81, 407, 2551, 8678]
F_nums4 = [1, 29, 32, 55, 94, 131, 443]
F_nums5 = [1, 2, 4, 5, 6, 7, 10, 11, 13, 14, 27]
F_nums6 = [1, 2, 3, 4, 5, 8, 9, 10, 12, 18, 37]
F_nums7 = [1, 3, 7, 8, 10, 11, 12, 16, 17, 18, 30, 32, 34, 61, 77, 123]
F_nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 23, 24, 28, 34, 49, 50, 124, 192, 208]

import pandas as pd

Fields = pd.DataFrame()

for satid in F_nums1:
        Fields = Fields.append(data1[data1['haloid']==satid])
for satid in F_nums2:
        Fields = Fields.append(data2[data2['haloid']==satid])
for satid in F_nums3:
        Fields = Fields.append(data3[data3['haloid']==satid])
for satid in F_nums4:
        Fields = Fields.append(data4[data4['haloid']==satid])
for satid in F_nums5:
        Fields = Fields.append(Cap_Marvel[Cap_Marvel['haloid']==satid])
for satid in F_nums6:
        Fields = Fields.append(Elektra[Elektra['haloid']==satid])
for satid in F_nums7:
        Fields = Fields.append(Rogue[Rogue['haloid']==satid])
for satid in F_nums8:
        Fields = Fields.append(Storm[Storm['haloid']==satid])
        
Sat = pd.DataFrame()

for satid in S_nums1:
        Sat = Sat.append(data1[data1['haloid']==satid])
for satid in S_nums2:
        Sat = Sat.append(data2[data2['haloid']==satid])
for satid in S_nums3:
        Sat = Sat.append(data3[data3['haloid']==satid])
for satid in S_nums4:
        Sat = Sat.append(data4[data4['haloid']==satid])
for satid in F_nums5:
        Fields = Fields.append(Cap_Marvel[Cap_Marvel['haloid']==satid])
for satid in F_nums6:
        Fields = Fields.append(Elektra[Elektra['haloid']==satid])
for satid in F_nums7:
        Fields = Fields.append(Rogue[Rogue['haloid']==satid])
for satid in F_nums8:
        Fields = Fields.append(Storm[Storm['haloid']==satid])
        
        
qF = Fields['sSFR'] < 2e-11
uF = ~qF
qS = Sat['sSFR'] < 2e-11
uS = ~qS
qD = data['sSFR'] < 2e-11
uD = ~qD

s = ~np.array(np.isnan(data['hostDist']))
q = np.array(data['sSFR'] <1e-11)
f = ~s
u = ~q