from intern.remote.dvid import DVIDRemote
import intern
from intern.remote.localFile import LocalRemote
from intern.remote.boss import BossRemote
from intern.resource.boss.resource import *
import matplotlib.pyplot as plt
import numpy as np
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

import ast
import codecs


api = "http://localhost:8000"

#CREATE REPOS
a = requests.post(api + "/api/repos",
    data=json.dumps({"Alias" : "LuisRTest1",
        "Description" : "Boss Uploaded data test"})
    )
cont = a.content
cont = ast.literal_eval(cont)
UUID = cont["root"]
print UUID

dat1 = requests.post(api + "/api/repo/" + UUID + "/instance" ,
	data=json.dumps({"typename" : "uint8blk",
		  "dataname" : "Luis1",
		  "versioned" : "0"
	}))
print(dat1.content)

# BOSS Data fetch:
boss = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88",
})
volumeB = boss.get_cutout(
    boss.get_channel("em", "pinky40", "v7"), 2,
    [10000, 10100], [10000, 10100], [501, 502],
)


volumeB = volumeB.tobytes()
print len(volumeB)

dif = (32*32*32) - len(volumeB)

volumeB = volumeB + str("".join((["0"]*dif)))
print len(volumeB)

# print len(data)

import requests
res = requests.post(
    api + "/api/node/" + UUID + "/Luis1/raw/0_1_2/{}_{}_{}/{}_{}_{}/".format(
     32,32,32,0,0,64
    ),
    data = volumeB
)
print(res.content)

dat = requests.get(api + '/api/node/' + UUID + '/Luis1/raw/0_1_2/32_32_32/0_0_64/octet-stream')
dat = dat.content
dat = dat[:(100*100*1)]
entire_space = np.fromstring(dat,dtype=np.uint8)

entire_space2 = entire_space.reshape(100,100,1)
volumeOut = entire_space2[:,:,0]

imgplot = plt.imshow(volumeOut, cmap = 'gray')
plt.show()


# entire_space2 = entire_space.reshape(32,32,32)

# r= requests.get('http://34.200.231.1/api/node/f40987727b384139bfd9b5e46c4a3a6c/repos/Luis3/raw/0_1_2/32_32_32/0_0_32/octet-stream')
# r = r.content
# entire_space = np.fromstring(r,dtype=np.uint8)
# print entire_space
# # entire_space2 = entire_space.reshape(32,32,32)




# volumeB = volumeB.astype('<U60')
# # # print volumeB
# volumeB = volumeB.tobytes()
# # if isinstance(volumeB, str):
# #     print 'ordinary string'
# # elif isinstance(volumeB, unicode):
# #     print "unicode string"
# # else:
# #     print "not a string"
#
# # volumeB = volumeB.encode('utf-8').strip()
#
# res = requests.post(
#     "http://localhost:8000/api/node/13597a0ebcd64cdc894fd21d05aad068/Luis3/raw/0_1_2/{}_{}_{}/{}_{}_{}".format(
#         512,256,256,0,0,32
#     ),
#     data= volumeB
# )
# print res.content
#
# # p = requests.post(api + "/node/" + UUID + "/" + volumeB + "/" + "tile/xy/0/10_10_20")
# # print p.content
#
#

# print(dvid.get_log("5cc94d532799484cb01788fcdb7cd9f0"))
# UUID = "b0d3e563a8b14e2e87543903a1233652"
#
# requests.delete(api+ "/api/repo/" + UUID + "?imsure=true")
#





# dat1 = requests.post(api + "/api/repo/"+ UUID + "/instance",
# data=json.dumps({"typename": typename,
#     "dataname" : dataname,
#     "versioned": version
# }))

# r = requests.get("http://localhost:8000/api/node/5cc94d532799484cb01788fcdb7cd9f0/grayscale/blocks/10_20_30/8")
# with open("code3.zip","wb") as code:
#     code.write(r.content)

# r = requests.get("http://localhost:8000/api/node/5cc94d532799484cb01788fcdb7cd9f0/grayscale/raw/0_1_2/2300_2300_1380/100_100_1/octet-stream")
# octet_stream = r.content
# print(octet_stream)


# #Converts obtained octet-stream into a numpy array of specified type uint8
# entire_space = np.fromstring(octet_stream,dtype=np.uint8)

# #Specifies the 3 dimensional shape of the numpy array of the size given by the user
# entire_space2 = entire_space.reshape(10,2300,2300)


# print(entire_space2)







# p = requests.post("http://localhost:8000/api/repos")
# print(type(p.content))
#
# # UUID = p.content
# # print(UUID)
#
# UUID = p["root"]
# print(UUID)





# UUID = "b47fbe5c5a10487c8c66337fc16d7201"

# # availability = requests.head("http://34.200.231.1/api/repo/" + UUID + "/info/")
# # print(availability.content)

# dat1 = requests.post("http://localhost:8000/api/repo/b47fbe5c5a10487c8c66337fc16d7201/instance",
# 	data=json.dumps({"typename": "uint8blk",
# 		"dataname" : "Luis1",
# 		"versioned": "1"
# 	}))

# print(dat1.content)

# dat1 = requests.post("http://34.200.231.1/api/repo/" + UUID + "/instance" ,
# 	data=json.dumps({"typename" : "uint8blk",
# 		  "dataname" : "Luis1",
# 		  "versioned" : "0"
# 	}))
# print(dat1.content)

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

# def chunkstring(string,length):
# 	return (string[0+i:length+i] for i in range(0,len(string),length))

# # print(back)
# # size = 3200,3200
# tst = './test1.jpg'
# im = Image.open(tst)
# # print(im)
# # im.thumbnail(size)
# # im.save("./" + ".thumbnail","JPEG")


# # im = '.thumbnail'
# ba = np.fromfile(tst,dtype='uint8')
# back = np.fromstring(ba,dtype=np.uint8)
# octet_stream = back.tobytes()
# octet_streamF = octet_stream + bytearray(1073741824-len(octet_stream))



# print(len(octet_stream))
# print(len(octet_streamF))
# # octet_streams = str("".join(["0"]*(10*10*10)))


# # octet_streams ="".join(["0"]*(512*256*256))

# # x = 10
# # y = 10
# # z = 10

# print("Loading...")

# # total_reshape = x*y*z
# # print(total_reshape)

# # info = requests.get(
# # 	"http://34.200.231.1/api/node/c7185f6c50b54cceaf4c4dec26bb6e0c/Luis3/metadata"
# # 	)
# # info = info.content
# # print(info)

dat = str("".join((["J"] * (32 * 32 * 32))))

# import requests
# res = requests.post(
#     "http://34.200.231.1/api/node/f40987727b384139bfd9b5e46c4a3a6c/Luis3/raw/0_1_2/{}_{}_{}/{}_{}_{}/".format(
#      32,32,32,0,0,32
#     ),
#     data= str(VolumeB)
# )
#
# print(res.content)
#
# r= requests.get('http://34.200.231.1/api/node/f40987727b384139bfd9b5e46c4a3a6c/repos/Luis3/raw/0_1_2/32_32_32/0_0_32/octet-stream')
# r = r.content
# entire_space = np.fromstring(r,dtype=np.uint8)
# print entire_space
# # entire_space2 = entire_space.reshape(32,32,32)

# dvid = DVIDRemote({
# 	"protocol": "http",
# 	"host": "localhost:8000",
# 	})
# #Gets 3d volume data
# volumeD = dvid.get_cutout(
# 	dvid.get_UUID("f40987727b384139bfd9b5e46c4a3a6c","Luis3"),
# 	[0,100],[0,100],[0,100]
# 	)
# print volumeD
# # import requests
# res = requests.post(
#     "http://localhost:8000/api/node/13597a0ebcd64cdc894fd21d05aad068/Luis3/raw/0_1_2/{}_{}_{}/{}_{}_{}/".format(
#         32,32,32,32,32,32
#     ),
#     data=str("".join((["J"] * (32 * 32 * 32))))
# )
# print res.content
