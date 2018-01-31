import intern
from intern.remote.dvid import DVIDRemote

from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

UUID = "5fa41dc158984c6d8b65ab2cfe7427b5"

#Declare DVIDRemote
dvid = DVIDRemote({
	"protocol": "http",
	"host": "localhost:8000",
    })

volumeD = dvid.get_cutout(
    dvid.get_channel(UUID, "Proj4", "dyer15_3_maskim"), 0,
    [0,2560], [0,2560], [31,32]
)
print volumeD
imgplot = plt.imshow(volumeD[:,:,0], cmap = 'gray')
plt.show()
