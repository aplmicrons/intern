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
import numpy as np

LATEST_VERSION = 'v0'
HOST = 'host'




class DVIDRemote(Remote):

	def __init__(self, cfg_file_or_dict=None, version=None):
		Remote.__init__(self,cfg_file_or_dict)
		if version is None:
			version = LATEST_VERSION

	def get_cutout(IP, IDtypev, shape, xpix, ypix, zpix, xo, yo, zo):
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
	    size = str(xpix) + "_" + str(ypix) + "_" +str(zpix)
	    offset = str(xo) + "_" + str(yo) + "_" + str(zo)
	    ID, typev = IDtypev

	    #User entered IP address with added octet-stream line to obtain data from api in octet-stream form
	    #0_1_2 specifies a 3 dimensional octet-stream "xy" "xz" "yz"
	    address = IP + "/" + ID + "/grayscale" + "/" + typev + "/" + shape + "/0_1_2" + size + "/" + offset + "/octet-stream" 
	    r = requests.get(address)
	    octet_stream = r.content

	    #Converts obtained octet-stream into a numpy array of specified type uint8
	    entire_space = np.fromstring(octet_stream,dtype=np.uint8)

	    #Specifies the 3 dimensional shape of the numpy array of the size given by the user
	    entire_space2 = entire_space.reshape(zpix,ypix,xpix)
	    #Returns a 3-dimensional numpy array to the user
	    return entire_space2




	# def create_cutout(self, resource, resolution, x_range, y_range, z_range, data, time_range=None):

 #        if not resource.valid_volume():
 #            raise RuntimeError('Resource incompatible with the volume service.')
 #        return self._volume.create_cutout(
 #            resource, resolution, x_range, y_range, z_range, data, time_range)
