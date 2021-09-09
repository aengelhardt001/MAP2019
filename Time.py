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
tsim1 = '/home/akinshol/Data/Timescales/DataFiles/h148'
tsim2 = '/home/akinshol/Data/Timescales/DataFiles/h229'
tsim3 = '/home/akinshol/Data/Timescales/DataFiles/h242'
tsim4 = '/home/akinshol/Data/Timescales/DataFiles/h329'

datat1 = []

with open(tsim1 + '.data', 'rb') as f:
    while True:
        try:
            datat1.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    datat1 = pd.DataFrame(datat1)

datat2 = []

with open(tsim2 + '.data', 'rb') as f:
    while True:
        try:
            datat2.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    datat2 = pd.DataFrame(datat2)
    
datat3 = []

with open(tsim3 + '.data', 'rb') as f:
    while True:
        try:
            datat3.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    datat3 = pd.DataFrame(datat3)
    
datat4 = []

with open(tsim4 + '.data', 'rb') as f:
    while True:
        try:
            datat4.append(pickle.load(f,encoding='latin1'))
        except EOFError:
            break
        
    datat4 = pd.DataFrame(datat4)








# st2 = pynbody.load(tsim_2)
# ht2 = st2.halos()
# st2.physical_units()

# st3 = pynbody.load(tsim_3)
# ht3 = st3.halos()
# st3.physical_units()

# st4 = pynbody.load(tsim_4)
# ht4 = st4.halos()
# st4.physical_units()




