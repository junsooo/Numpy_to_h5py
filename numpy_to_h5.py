#Numpy array to h5 file
#http://stackoverflow.com/questions/20928136/input-and-output-numpy-arrays-to-h5py

import numpy as np
import h5py

st = []
st = np.hstack((12.3,st))
st = np.hstack((23.4,st))
st = np.hstack((34.5,st))	#st == array([ 34.5,  23.4,  12.3])

#Open and store h5py file 'data.h5'
h5f = h5py.File('data.h5','w')
h5f.create_dataset('dataset_1',data=st)
h5f.close()

#Load h5py file 'data.h5'
h5f = h5py.File('data.h5','r')
b = h5f['dataset_1'][:]	#b == array([ 34.5,  23.4,  12.3])
h5f.close()
