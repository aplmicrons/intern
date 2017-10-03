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
import json
import math

# from intern.resource.dvid.resource import *
from intern.service.dvid.service import *


LATEST_VERSION = 'v0'
CONFIG_PROTOCOL = 'protocol'
CONFIG_HOST = 'host'
api = ""


class DVIDRemote(Remote):

	def __init__(self, specs, version=None):
		"""
			Constructor.

			Checks for latest version. If no version is given, assigns version as none
			Protocol and host specifications are taken in as keys -values of dictionary.
			global api variable is named and used for every command that requires api.
		"""

		if version is None:
			version = LATEST_VERSION

		protocol = specs[CONFIG_HOST]
		host = specs[CONFIG_PROTOCOL]


		global api
		api = host + "://" + protocol
		

	def get_channel(self, ID, repos):
		#obtains ID and repos and converts the input into a touple
		IDrepos = (ID, repos)
		return IDrepos

	def get_cutout(self, IDrepos, xspan, yspan, zspan):
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

	    #Defining used variables
	    xpix = xspan[1]-xspan[0]
	    xo = xspan[0]

	    ypix = yspan[1]-yspan[0]
	    yo = yspan[0]

	    zpix = zspan[1]-zspan[0]
	    zo = zspan[0]

	    size = str(xpix) + "_" + str(ypix) + "_" + str(zpix)
	    offset = str(xo) + "_" + str(yo) + "_" + str(zo)
	    ID, repos = IDrepos
	    #User entered IP address with added octet-stream line to obtain data from api in octet-stream form
	    #0_1_2 specifies a 3 dimensional octet-stream "xy" "xz" "yz"

	    address = api + "/api/node/" + ID + "/" + repos + "/raw" + "/0_1_2/" + size + "/" + offset + "/octet-stream" 
	    r = requests.get(address)
	    octet_stream = r.content

	    #Converts obtained octet-stream into a numpy array of specified type uint8
	    entire_space = np.fromstring(octet_stream,dtype=np.uint8)

	    #Specifies the 3 dimensional shape of the numpy array of the size given by the user
	    entire_space2 = entire_space.reshape(zpix,ypix,xpix)

	    #Returns a 3-dimensional numpy array to the user
	    return entire_space2


	def create_project(self, typename,dataname,version=0):
		#Creates a repository for the data to be placed in.
		#Returns randomly generated 32 character long UUID
		a = requests.post(api + "/api/repos")
		UUID = a["root"]

		dat1 = requests.post(api + "/api/repo/"+ UUID + "/instance",
			data=json.dumps({"typename": typename,
				"dataname" : dataname,
				"versioned": version
			}))

		return ("This is you UUID: " + UUID + "." + dat1.content)

	def create_cutout(self,UUID,typename,dataname,version=0):
		#Creates an instance which works as a sub-folder where the data is stored
		#Must specify:
		#typename(required) = "uint8blk", "labelblk", "labelvol", "imagetile"
		#dataname(required) = "example1"
		#version(required) = "1"
		#The size of the space reserved must be a cube with sides of multiples of 32

		dat1 = requests.post(api + "/api/repo/" + UUID + "/instance", 
			json = ({"typename" : typename,
				"dataname" : dataname,
				"versioned" : version
		}))
		res = requests.post(
			api + "/api/node/" + UUID + "/"+ dataname +"Luis3/raw/0_1_2/{}_{}_{}/{}_{}_{}/".format(
				x,y,z,32,32,32
				),
			data=octet_streams
			)
		return("Your data has been uploaded to the cutout in " + dataname)

	def get_info(self, UUID):
		#Returns JSON for just the repository with given root UUID.  The UUID string can be
		#shortened as long as it is uniquely identifiable across the managed repositories.
		return DvidService.get_info(api,UUID)

	def get_log(self, UUID):
		#The log is a list of strings that will be appended to the repo's log.  They should be
		#descriptions for the entire repo and not just one node.  For particular versions, use
		#node-level logging (below).
		return DvidService.get_log(api,UUID)

	def post_log(self, UUID,log1):
		#Allows the user to write a short description of the content in the repository
		#{ "log": [ "provenance data...", "provenance data...", ...] }
		return DvidService.post_log(api,UUID)

	def get_server_info(self):
		#Returns JSON for server properties
		return DvidService.get_server_info(api,UUID)

	def change_server_setting(self,gc1,throt1):
		#	Sets server parameters.  Expects JSON to be posted with optional keys denoting parameters:
		return DvidService.change_server_setting(api,UUID)
		