from intern.remote.dvid import DVIDRemote
import matplotlib.pyplot as plt
import os
import platform
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy


#THIS CURRENTLY WORKS ONLY UNDER THE FORKED VERSION OF INTERN on APLmicrons/intern. SO make sure you install that version onto your Site_packages :)

volume = DVIDRemote.get_cutout("http://34.200.231.1/api/node","5cc94d532799484cb01788fcdb7cd9f0", "grayscale", "raw", "xy", 2000, 2100, 5, 2000, 2100, 1380)
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