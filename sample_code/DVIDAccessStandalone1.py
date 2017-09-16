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

# UUID = DVIDRemote.create_project("http://34.200.231.1","uint8blk","Luis4")
UUID = "f40987727b384139bfd9b5e46c4a3a6c"
availability = DVIDRemote.get_info(UUID)
print(availability)

# dvid = DVIDRemote({
# 	'protocol': 'https',
# 	'host':'34.200.231.1',
# 	'uuid':UUID,
# 	})

# volume = dvid.get_cutout()

volume = DVIDRemote.get_cutout("http://34.200.231.1/api/node/",
	(UUID, "Luis3"),
	512,256,256,256,0,0)

#Demonstration of obtaining and updating the log
log = DVIDRemote.get_log(UUID)
print(log)
logP = DVIDRemote.post_log(UUID,"This repository contains images used for testing")
print(logP)
log = DVIDRemote.get_log(UUID)
print(log)

print(volume)

figure1 = plt.figure(1)
plt.imshow(volume[0,:,:])
# # figure2 = plt.figure(2)
# # plt.imshow(volume[4,:,:],cmap="gray")
plt.show()