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

# UUID = "b47fbe5c5a10487c8c66337fc16d7201"
# mes = dvid.create_project("uint8blk","Luis4","1")
# print(mes)

# #Getting information on the UUID
# info = dvid.get_info(UUID)
# print(info)

# # Demonstration of obtaining and updating the log
# log = dvid.get_log(UUID)
# print(log)
# logP = dvid.post_log(UUID,"This repository contains images used for testing")
# log = dvid.get_log(UUID)
# print(log)


#Gets 3d volume data
volumeD = dvid.get_cutout(
	dvid.get_channel("5cc94d532799484cb01788fcdb7cd9f0","grayscale"),
	[2300,4600],[2300,4600],[1380,1390]
	)

# print(volumeD)

# figure1 = plt.figure(1)
# plt.imshow(volume[0,:,:])
# # # figure2 = plt.figure(2)
# # # plt.imshow(volume[4,:,:],cmap="gray")
# plt.show()