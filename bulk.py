import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Tahoma','Lucida Grande','Verdana', 'DejaVu Sans']

def read_file(simpath,simname):
    ### leave this section as is
    data = []
    with open(simpath + '.data', 'rb') as f:
        while True:
            try:
                data.append(pickle.load(f,encoding='latin1'))
            except EOFError:
                break
        data1 = pd.DataFrame(data)
        data1['sim'] = [simname]*len(data1)
        data1['g-r'] = 1.646*(data1['V_mag'] - data1['R_mag']) - 0.139
        return data1
    
def read_all():
	sim1 = '/home/akinshol/Data/Sims/h148.cosmo50PLK.3072g3HbwK1BH/h148.cosmo50PLK.3072g3HbwK1BH.004096/h148.cosmo50PLK.3072g3HbwK1BH.004096'
	sim2 = '/home/akinshol/Data/Sims/h229.cosmo50PLK.3072gst5HbwK1BH/h229.cosmo50PLK.3072gst5HbwK1BH.004096/h229.cosmo50PLK.3072gst5HbwK1BH.004096'
	sim3 = '/home/akinshol/Data/Sims/h242.cosmo50PLK.3072gst5HbwK1BH/h242.cosmo50PLK.3072gst5HbwK1BH.004096/h242.cosmo50PLK.3072gst5HbwK1BH.004096'
	sim4 = '/home/akinshol/Data/Sims/h329.cosmo50PLK.3072gst5HbwK1BH/h329.cosmo50PLK.3072gst5HbwK1BH.004096/h329.cosmo50PLK.3072gst5HbwK1BH.004096'
	data = read_file(sim1,'h148')
	data = data.append(read_file(sim2,'h229'))
	data = data.append(read_file(sim3,'h242'))
	data = data.append(read_file(sim4,'h329'))
	return data

def quenched(data):
    return np.array((data['sSFR'] <= 1e-10) & (data['HIgasfrac'] <= 0.2))
#     output = []
#     for i in range(len(data)):
#         if data['sSFR'].tolist()[i] <= 1e-10 and data['HIgasfrac'].tolist()[i] <= 0.2:
#             output.append(True)
#         else:
#             output.append(False)
#     return np.array(output)
    
def sat(data,whichhost=False):
    output = []
    hostid = []
    for i in range(len(data)):
        if data['sim'].tolist()[i]=='h148' or data['sim'].tolist()[i]=='h242':
            if data['hostHalo'].tolist()[i]==-1:
                output.append(False)
                hostid.append(-1)
            else:
                output.append(True)
                hostid.append(data['haloid'][np.array(data['id2'])==np.array(data['hostHalo'].tolist()[i])].tolist()[0])
        elif data['sim'].tolist()[i]=='h229' or data['sim'].tolist()[i]=='h329':
            if data['hostHalo'].tolist()[i]==0:
                output.append(False)
                hostid.append(-1)
            else:
                output.append(True)
                hostid.append(data['haloid'][np.array(data['id2'])==np.array(data['hostHalo'].tolist()[i])].tolist()[0])
        else: 
            raise Exception("simname must be either 'h148','h229','h242','h329'")
    
    if whichhost:
        return np.array(hostid)
    else:
        return np.array(output)
    
def whichHost(data):
    return sat(data,whichhost=True)

def distance_to_nearest_halo(data):
    distances = []
    for i in range(len(data)):
        halocoords = np.array([data['Xc'].tolist()[i],data['Yc'].tolist()[i],data['Zc'].tolist()[i]])
        nstars = np.delete(data['n_star'].tolist(),i)
        x = np.delete(data['Xc'].tolist(),i)
        y = np.delete(data['Yc'].tolist(),i)
        z = np.delete(data['Zc'].tolist(),i)
        x = x[nstars >= 100].tolist()
        y = y[nstars >= 100].tolist()
        z = z[nstars >= 100].tolist()
        coords = np.array([x,y,z])
        coords = np.transpose(coords)
        dist = np.min(np.sqrt(np.sum((halocoords - coords)**2, axis=1)))
        distances.append(dist)
    return np.array(distances)

def distance_to_host(data,rvir=True):
    '''
    Returns an array of the distances to host galaxies for all halos in `data`. 
    Optional argument `rvir` changes whether or not to divide distance by host virial radius.
    '''
    distances = []
    for i in range(len(data)):
        host = whichHost(data)[i]
        if host == -1:
            distances.append(0)
        else:
            halocoords = np.array([data['Xc'].tolist()[i],data['Yc'].tolist()[i],data['Zc'].tolist()[i]])
            hostcoords = np.array([data['Xc'][data['haloid']==host].tolist()[0],data['Yc'][data['haloid']==host].tolist()[0],data['Zc'][data['haloid']==host].tolist()[0]])
            if rvir:
                if data['sim'].tolist()[i]=='h148':
                    r = data['Rvir'][(data['haloid']==host) & (data['sim']=='h148')].tolist()[0]
                elif data['sim'].tolist()[i]=='h229':
                    r = data['Rvir'][(data['haloid']==host) & (data['sim']=='h229')].tolist()[0]
                elif data['sim'].tolist()[i]=='h242':
                    r = data['Rvir'][(data['haloid']==host) & (data['sim']=='h242')].tolist()[0]
                elif data['sim'].tolist()[i]=='h329':
                    r = data['Rvir'][(data['haloid']==host) & (data['sim']=='h329')].tolist()[0]
                distances.append(np.sqrt(np.sum((hostcoords - halocoords)**2))/r)
            else:
                distances.append(np.sqrt(np.sum((hostcoords - halocoords)**2)))
    return np.array(distances)

def distance_to_nearest_host(data):
    distances = []
    for i in range(len(data)):
        halocoords = np.array([data['Xc'].tolist()[i],data['Yc'].tolist()[i],data['Zc'].tolist()[i]])
        nstars = np.delete(data['n_star'].tolist(),i)
        notsat = np.delete(~np.array(sat(data)),i)
        x = np.delete(data['Xc'].tolist(),i)
        y = np.delete(data['Yc'].tolist(),i)
        z = np.delete(data['Zc'].tolist(),i)
        x = x[nstars >= 100 & notsat].tolist()
        y = y[nstars >= 100 & notsat].tolist()
        z = z[nstars >= 100 & notsat].tolist()
        coords = np.array([x,y,z])
        coords = np.transpose(coords)
        dist = np.min(np.sqrt(np.sum((halocoords - coords)**2, axis=1)))
        distances.append(dist)
    return np.array(distances)