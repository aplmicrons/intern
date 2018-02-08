import intern
from intern.remote.dvid import DVIDRemote

from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

UUID = "30eb"

#Declare DVIDRemote
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
    })

volumeD = dvid.get_cutout(
    dvid.get_channel(UUID, "dyer15_3_maskim_DUmmy", "dyer15_3_maskim_DUmmy"), 0,
    [0,2560], [0,2560], [290,292]
)
print(volumeD)
imgplot = plt.imshow(volumeD[0,:,:], cmap = 'gray')
plt.show()
