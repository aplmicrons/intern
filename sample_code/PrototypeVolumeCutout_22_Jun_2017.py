import matplotlib.pyplot as plt
import os
import platform
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from io import BytesIO
import numpy

"""
@author Shain Bannowsky
@date 22 June 2017
"""

# Python method for extracting a volume from DIVD
# Place inside DVID remove class, in file remote.py, after get_cutout() method

    # This function outputs a 3D numpy array of volume data
    # Arguemnts are similar to egt_cutout, with the addition of zpix
def get_cutout(IP, ID, scale, typev, shape, xpix, ypix, zpix, xo, yo, zo):
	    #ID MUST BE STRING ""
	    #SCALE MUST BE STRING "" - "GRAYSCALE"
	    #TYPEV MUST BE STRING "" - "RAW"
	    #SHAPE MUST BE STRING "" - 'XY'
	    #self.resource = resource
	    # self.resolution = resolution
	    # self.x_range = x_range
	    # self.y_range = y_range
	    # self.z_range = z_range
	    #shape = "xy"
	    #xpix = "x" how many pixels traveled in x
	    #ypix = "y" how many pixels traveled in y
       #zpix = "z" how many pixels traveled in z
	    #xo, yo, zo (x,y,z offsets)
	    #type = "raw"
	    #scale = "grayscale"
        
        # Sanity check
    if (type(zpix) == int) and zpix != 0:
            
            # Initalizing z offset
        z_offset = zo
            
            # Initalizing output array
        output = get_plane(IP, ID, scale, typev, shape, xpix, ypix, xo, yo, z_offset)

            # Iterating variable
        i = 1
            
            # Iterating
        while i < abs(zpix):
            z_offset = int(z_offset + (zpix / abs(zpix)))
            i =i +1
            plane = get_plane(IP, ID, scale, typev, shape, xpix, ypix, xo, yo, z_offset)
            output = [output,plane]
    
    outputnp = numpy.vstack(output)
    return outputnp

def get_plane(IP, ID, scale, typev, shape, xpix, ypix, xo, yo, zo):
    #ID MUST BE STRING ""
    #SCALE MUST BE STRING "" - "GRAYSCALE"
    #TYPEV MUST BE STRING "" - "RAW"
    #SHAPE MUST BE STRING "" - 'XY'
    #self.resource = resource
    # self.resolution = resolution
    # self.x_range = x_range
    # self.y_range = y_range
    # self.z_range = z_range
    #shape = "xy"
    #xpix = "x" how much pixels traveled in x
    #ypix = "y" how much pixels traveled in y
    #xo, yo, zo (x,y,z offsets)
    #type = "raw"
    #scale = "grayscale"
    size = str(xpix) + "_" + str(ypix)
    offset = str(xo) + "_" + str(yo) + "_" + str(zo)

    address = IP + "/" + ID + "/" + scale + "/" + typev + "/" + shape + "/" + size + "/" + offset
    r = requests.get(address)
    bytes1 = r.content
    stream = BytesIO(bytes1)
    img = Image.open(stream)
    a = numpy.asarray(img)

    return a

volume = get_cutout("http://34.200.231.1/api/node","5cc94d532799484cb01788fcdb7cd9f0", "grayscale", "raw", "xy", 2000, 2100, 5, 2000, 2100, 1380)
print(volume)

image2= Image.fromarray(volume[1])

image2.save("test1.png")

# Opening file with platform specific command
sysname = platform.system()
if sysname == 'Darwin':
    os.system('open test1.png')
elif sysname == 'Windows':
    os.system('start test1.png')
else:
    os.system('open test1.png')