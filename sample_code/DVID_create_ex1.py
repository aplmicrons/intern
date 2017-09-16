import requests
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from io import BytesIO

r = requests.get("http://34.200.231.1/api/node/5cc94d532799484cb01788fcdb7cd9f0/grayscale/raw/0_1_2/4000_4000_10/2400_2400_1380/octet-stream")

octet_stream = r.content
# print(octet_stream)
entire_space = np.fromstring(octet_stream,dtype=np.uint8)
entire_space2 = entire_space.reshape(10,4000,4000)


# np.set_printoptions(threshold = np.nan)
print(entire_space.shape)
print(entire_space.size)

print(entire_space2)
print(entire_space2.shape)
plt.imshow(entire_space2[1,:,:], cmap = 'gray')
plt.show()


# e_s = entire_space.size
# a = 0
# n = 0
# i = 0
# while i <= e_s:
# 	if a < e_s:
# 		if entire_space[a] == 0 :
# 			entire_space = np.delete(entire_space,a)
# 			e_s = entire_space.size
# 			a = a
# 			i = i
# 		else:
# 			a = a+1
# 			i = i+1
# 	else:
# 		i = e_s+1

# print(entire_space.shape)
# print(entire_space.size)

# entire_space2 = entire_space.reshape(256,512,512)

# print(entire_space2)
# print(entire_space2.shape)
# plt.imshow(entire_space2[2,:,:])
# plt.show()
