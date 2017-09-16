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
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from io import BytesIO
import json
from PIL import Image
import math
# p = requests.post("http://34.200.231.1/api/repos")
# UUID = p.content
# print(UUID)
UUID = "f40987727b384139bfd9b5e46c4a3a6c"

# availability = requests.head("http://34.200.231.1/api/repo/" + UUID + "/info/")
# print(availability.content)

dat1 = requests.post("http://34.200.231.1/api/repo/" + UUID + "/instance" , 
	data=json.dumps({"typename" : "uint8blk",
		  "dataname" : "Luis3",
		  "versioned" : "0"
	}))
print(dat1.content)

# lab = requests.post("http://34.200.231.1/api/repo/" + UUID + "/instance" , 
# 	data=json.dumps({"typename" : "labelblk",
# 		  "dataname" : "labels3",
# 		  "sync" : "bodies3"
# 	}))
# print(lab.content)

# bod = requests.post("http://34.200.231.1/api/repo/" + UUID + "/instance" , 
# 	data=json.dumps({"typename" : "labelvol",
# 		  "dataname" : "bodies3",
# 		  "sync" : "labels3"
# 	}))
# print(bod.content)

# gtile = requests.post("http://34.200.231.1/api/repo/" + UUID + "/instance" , 
# 	data=json.dumps({"typename" : "imagetile",
# 		  "dataname" : "luistiles3",
# 		  "compression" : "none",
# 		  "source" : "Luis3",
# 		  "format" : "jpg"
# 	})

# )
# print(gtile.content)

def chunkstring(string,length):
	return (string[0+i:length+i] for i in range(0,len(string),length))

# print(back)
# size = 3200,3200
tst = './test1.jpg'
im = Image.open(tst)
# print(im)
# im.thumbnail(size)
# im.save("./" + ".thumbnail","JPEG")


# im = '.thumbnail'
ba = np.fromfile(tst,dtype='uint8')
back = np.fromstring(ba,dtype=np.uint8)
octet_stream = back.tobytes()
octet_streamF = octet_stream + bytearray(1073741824-len(octet_stream))



print(len(octet_stream))
print(len(octet_streamF))
# octet_streams = str("".join(["0"]*(10*10*10)))


# octet_streams ="".join(["0"]*(512*256*256))

# x = 10
# y = 10
# z = 10

print("Loading...")

# total_reshape = x*y*z
# print(total_reshape)

# info = requests.get(
# 	"http://34.200.231.1/api/node/c7185f6c50b54cceaf4c4dec26bb6e0c/Luis3/metadata"
# 	)
# info = info.content
# print(info)


res = requests.post(
    "http://34.200.231.1/api/node/f40987727b384139bfd9b5e46c4a3a6c/Luis3/raw/0_1_2/{}_{}_{}/{}_{}_{}/".format(
        1048576,32,32,0,0,0
    ),
    data=octet_streamF,
    headers = {'Content-Type' : 'application/octet-stream'}
)
print(res.content)

# res = requests.post(
#     "http://34.200.231.1/api/node/c7185f6c50b54cceaf4c4dec26bb6e0c/Luis3/raw/0_1_2/{}_{}_{}/{}_{}_{}/".format(
#         512,256,256,0,0,32
#     ),
#     data=str("".join((["J"] * (512 * 256 * 256))))
# )
# print(res)