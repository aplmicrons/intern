import requests
import os
import platform
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
# from StringIO import StringIO

def get_cutout(ID, scale, typev, shape, xpix, ypix, xo, yo, zo):
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

    address = "http://34.200.231.1/api/node/" + ID + "/" + scale + "/" + typev + "/" + shape + "/" + size + "/" + offset
    r = requests.get(address)
    bytes1 = r.content
    stream = BytesIO(bytes1)
    img = Image.open(stream)
    a = numpy.asarray(img)
    return a


volume = get_cutout("5cc94d532799484cb01788fcdb7cd9f0", "grayscale", "raw", "xy", 2000, 2100, 2000, 2100, 1380)

print(volume)

image2= Image.fromarray(volume)

image2.save("test1.png")

# Opening file with platform specific command
sysname = platform.system()
if sysname == 'Darwin':
    os.system('open test1.png')
elif sysname == 'Windows':
    os.system('start test1.png')
else:
    os.system('open test1.png')