import intern
from intern.remote.dvid import DVIDRemote

from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

directory = '/Users/rodrilm2/Documents/APL/GeorgiaTech/proj4_masked/proj4_masked_390_593/'
data = np.zeros((2560,2560))

for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        pathname = os.path.join(directory,filename)
        print 'Processing:  ' + filename
        img = Image.open(pathname)
        newImArray = np.array(img)
        data= np.dstack((data,newImArray))
    else:
        print 'No images found in this directory'

#UPLOAD TO LOCAL REPOSITORY
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
    })

chan_setup = local.get_channel('Proj4','masked')
proj = local.create_project(chan_setup)
volume = local.create_cutout(proj,'390_593',data)
