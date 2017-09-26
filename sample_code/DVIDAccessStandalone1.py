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


UUID = "f40987727b384139bfd9b5e46c4a3a6c"
#UUID = DVIDRemote.create_project("http://34.200.231.1","uint8blk","Luis4")

#DVID Data fetch:
dvid = DVIDRemote({
	"protocol": "https",
	"host": "34.200.231.1",
	})

info = dvid.get_info(UUID)
print(info)

volumeD = requests.get("https://34.200.231.1/node/f40987727b384139bfd9b5e46c4a3a6c/grayscale/raw/2300_2300_10/2300_2300_1380/octet-stream")



# volumeD = dvid.get_cutout(
# 	dvid.get_channel("5cc94d532799484cb01788fcdb7cd9f0","grayscale"),
# 	[2300,4600],[2300,4600],[1380,1390]
# 	)

# #Demonstration of obtaining and updating the log
# log = DVIDRemote.get_log(UUID)
# print(log)
# logP = DVIDRemote.post_log(UUID,"This repository contains images used for testing")
# print(logP)
# log = DVIDRemote.get_log(UUID)
# print(log)

# print(volume)

# figure1 = plt.figure(1)
# plt.imshow(volume[0,:,:])
# # # figure2 = plt.figure(2)
# # # plt.imshow(volume[4,:,:],cmap="gray")
# plt.show()