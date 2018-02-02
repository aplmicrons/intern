import intern
from intern.remote.boss import BossRemote
from intern.resource.boss.resource import ChannelResource
from intern.remote.dvid import DVIDRemote
import matplotlib.pyplot as plt
import numpy as np

#DVID Data fetch:
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
	})
volumeD = dvid.get_cutoutI(
	dvid.get_channel("f324a674249d490081971b8d1371f39f","dyer15_3_maskim"),0,
	[0,2560],[0,2560],[390,400]
	)

#Printing volumes:
print("Dvid volume: ")
print(volumeD)

#Graphing Dvid:
imgplot = plt.imshow(volumeD[3,:,:], cmap = "gray")
plt.show()
