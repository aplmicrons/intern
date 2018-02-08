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
volumeD = dvid.get_cutout(
	dvid.get_channel("3ca15f84b1ee4fb780fef94c5771ffe6","dyer15_3_maskim"),0,
	[1287,1387],[1200,1300],[390,490]
	)

#Printing volumes:
print("Dvid volume: ")
print(volumeD)

#Graphing Dvid:
imgplot = plt.imshow(volumeD[3,:,:], cmap = "gray")
plt.show()
