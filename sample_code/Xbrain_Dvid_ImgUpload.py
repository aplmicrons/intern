import intern
from intern.remote.dvid import DVIDRemote

from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

iNumS = 390 #Image Number start
iNumE = 2014 #Image Number end
start = 0
end = 32

#Declare DVIDRemote
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
    })

chan_setup = dvid.ChannelResource('Proj4','dyer15_3_maskim', 'Data uploaded from XBrain experiments')
proj = dvid.create_project(chan_setup)
# UUID = chan_setup.split("/")
# UUID = UUID[0]

while iNumS <= iNumE:
    directory = '/Users/rodrilm2/Documents/APL/GeorgiaTech/proj4_masked_390_2014/'
    # data = np.zeros((2560,2560))
    num = format(iNumS, "04")
    filename = "dyer15_3_maskimg_" + num + ".tif"
    pathname = os.path.join(directory,filename)
    print 'Processing:  ' + filename
    img = Image.open(pathname)
    data = np.array(img)
    xrang = [0, 256]
    yrang = [0, 256]
    zrang = [start,end]
    volume = dvid.create_cutout(proj,xrang,yrang,zrang,data)
    start = start + 32
    end = end + 32
    iNumS = iNumS + 1

print end
