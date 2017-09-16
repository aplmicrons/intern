import requests
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from io import BytesIO

# r = requests.get("http://34.200.231.1/api/node/5cc94d532799484cb01788fcdb7cd9f0/grayscale/raw/0_1_2/4000_4000_10/2400_2400_1380/octet-stream")

xpix = 4000
ypix = 4000
zpix = 10
xo = 2400
yo = 2400
zo = 1380
IDtypev = ("5cc94d532799484cb01788fcdb7cd9f0" , "raw") 
IP = "http://34.200.231.1/api/node/"

size = str(xpix) + "_" + str(ypix) + "_" +str(zpix)
offset = str(xo) + "_" + str(yo) + "_" + str(zo)
ID, typev = IDtypev

#User entered IP address with added octet-stream line to obtain data from api in octet-stream form
#0_1_2 specifies a 3 dimensional octet-stream "xy" "xz" "yz"
address = IP + "/" + ID + "/grayscale" + "/" + typev + "/0_1_2/" + size + "/" + offset + "/octet-stream" 
r = requests.get(address)

octet_stream = r.content
print(octet_stream)
#Converts obtained octet-stream into a numpy array of specified type uint8
entire_space = np.fromstring(octet_stream,dtype=np.uint8)

#Specifies the 3 dimensional shape of the numpy array of the size given by the user
entire_space2 = entire_space.reshape(zpix,ypix,xpix)


# np.set_printoptions(threshold = np.nan)
print(entire_space.shape)
print(entire_space.size)

print(entire_space2)
print(entire_space2.shape)
plt.imshow(entire_space2[1,:,:], cmap = 'gray')
plt.show()
