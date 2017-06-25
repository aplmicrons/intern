"""
# Copyright 2017 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
from intern.remote import Remote
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

LATEST_VERSION = 'v0'

class DVIDRemote(Remote):

	def __init__(self, cfg_file_or_dict=None, version=None):
		Remote.__init__(self,cfg_file_or_dict)
		if version is None:
			version = LATEST_VERSION
		

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

	    #User entered IP address
	    address = IP + "/" + ID + "/" + scale + "/" + typev + "/" + shape + "/" + size + "/" + offset
	    r = requests.get(address)
	    bytes1 = r.content
	    stream = BytesIO(bytes1)
	    img = Image.open(stream)
	    a = numpy.asarray(img)

	    #This will output a 2D numpy array
	    return a

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

	    #Sanity check:
	    if (type(zpix) == int) and zpix != 0:
	    	
	    	# Initalizing z offset
	    	z_offset = zo
	    	
	    	# Initalizing output array
	    	output = DVIDRemote.get_plane(IP, ID, scale, typev, shape, xpix, ypix, xo, yo, z_offset)
	    	
	    	# Iterating variable
	    	i = 1
	    	
	    	# Iterating
	    	while i < abs(zpix):
	    		z_offset = int(z_offset + (zpix / abs(zpix)))
	    		i =i +1
	    		plane = DVIDRemote.get_plane(IP, ID, scale, typev, shape, xpix, ypix, xo, yo, z_offset)
	    		output = [output,plane]

	    	outputnp = numpy.array(output)

	    	#WIll output a 3D numpy array
	    	return outputnp


	# def create_cutout(self, resource, resolution, x_range, y_range, z_range, data, time_range=None):
	       
 #        if not resource.valid_volume():
 #            raise RuntimeError('Resource incompatible with the volume service.')
 #        return self._volume.create_cutout(
 #            resource, resolution, x_range, y_range, z_range, data, time_range)
