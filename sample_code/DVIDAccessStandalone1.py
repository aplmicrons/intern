#Before running this program you should make sure to have the correct version of intern installed on your device.
from intern.remote.dvid import DVIDRemote
import intern
import matplotlib.pyplot as plt
import os
import platform
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
import requests
import time


#DVID Data fetch:
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
	})

UUID = "5cc94d532799484cb01788fcdb7cd9f0"
# mes = dvid.create_project("uint8blk","Luis4","1")
# print(mes)

#Getting information on the UUID
info = dvid.get_info(UUID)
print(info)

# Demonstration of obtaining and updating the log
log = dvid.get_log(UUID)
print(log)
logP = dvid.post_log(UUID,"This repository contains images used for testing2")
log = dvid.get_log(UUID)
print(log)


#Gets 3d volume data
volumeD = dvid.get_cutout(
	dvid.get_UUID("5cc94d532799484cb01788fcdb7cd9f0","grayscale"),
	[2300,4600],[2300,4600],[1380,1390]
	)
print(volumeD)

imgplot = plt.imshow(volumeD[9,:,:])
plt.show()
imgplot = plt.imshow(volumeD[8,:,:])
plt.show()
imgplot = plt.imshow(volumeD[7,:,:])
plt.show()
imgplot = plt.imshow(volumeD[6,:,:])
plt.show()
imgplot = plt.imshow(volumeD[5,:,:])
plt.show()
imgplot = plt.imshow(volumeD[4,:,:])
plt.show()
imgplot = plt.imshow(volumeD[3,:,:])
plt.show()
imgplot = plt.imshow(volumeD[2,:,:])
plt.show()
imgplot = plt.imshow(volumeD[1,:,:])
plt.show()
imgplot = plt.imshow(volumeD[0,:,:])
plt.show()
