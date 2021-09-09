import numpy as np
import pynbody
import matplotlib.pyplot as plt
import matplotlib as mpl
import pynbody.plot as pp
import pickle
import pandas as pd
import pynbody.plot.sph as sph

sim_1 ='/home/akinshol/Data/Sims/h148.cosmo50PLK.3072g3HbwK1BH/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096'
s1 = pynbody.load(sim_1)
h1 = s1.halos()
s1.physical_units()


sim_2 ='/home/akinshol/Data/Sims/h229.cosmo50PLK.3072gst5HbwK1BH/h229.cosmo50PLK.3072gst5HbwK1BH.004096/h229.cosmo50PLK.3072gst5HbwK1BH.004096'
s2 = pynbody.load(sim_2)
h2 = s2.halos()
s2.physical_units()


sim_3 ='/home/akinshol/Data/Sims/newh242/h242.cosmo50PLK.3072gst5HbwK1BH.004096'
s3 = pynbody.load(sim_3)
h3 = s3.halos()
s3.physical_units()


sim_4 ='/home/akinshol/Data/Sims/newh329/h329.cosmo50PLK.3072gst5HbwK1BH.004096'
s4 = pynbody.load(sim_4)
h4 = s4.halos()
s4.physical_units()

sim_CM ='/home/akinshol/Data/Sims/cptmarvel.cosmo25cmb.4096g5HbwK1BH/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096.dir/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096'
s5 = pynbody.load(sim_CM)
h5 = s5.halos()
s5.physical_units()

sim_E ='/home/akinshol/Data/Sims/elektra.cosmo25cmb.4096g5HbwK1BH/elektra.cosmo25cmb.4096g5HbwK1BH.004096.dir/elektra.cosmo25cmb.4096g5HbwK1BH.004096'
s6 = pynbody.load(sim_E)
h6 = s6.halos()
s6.physical_units()

sim_R ='/home/akinshol/Data/Sims/rogue.cosmo25cmb.4096g5HbwK1BH/rogue.cosmo25cmb.4096g5HbwK1BH.004096.dir/rogue.cosmo25cmb.4096g5HbwK1BH.004096'
s7 = pynbody.load(sim_E)
h7 = s7.halos()
s7.physical_units()

sim_S ='/home/akinshol/Data/Sims/storm.cosmo25cmb.4096g5HbwK1BH/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096'
s8 = pynbody.load(sim_S)
h8 = s8.halos()
s8.physical_units()