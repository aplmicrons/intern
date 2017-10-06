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
from intern.resource.dvid.resource import *
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
		"""
			Method to obtain requested channel

			Args:
				ID : UUID assigned to DVID repository
				repos: name of the repository assigned by the user when instance was created

			Returns:
				Touple

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.get_channel(ID,repos)

	def get_cutout(self, IDrepos, xspan, yspan, zspan):
		"""
			Method to request a volume of data from dvid server

			Args:
				IDrepos : UUID assigned to DVID repository and repository name (touple)
				xspan : range of pixels in x axis ([1000:1500])
				yspan : range of pixels in y axis ([1000:1500])
				zspan : range of pixels in z axis ([1000:1010])

			Returns:
				array: numpy array representation of the requested volume

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.get_cutout(api,IDrepos,xspan,yspan,zspan)


	def create_project(self, typename,dataname,version=0):
		"""
			Method to create a project space in the dvid server

			Args:
				typename: describes data type stored (labelblk, labelvol, imagetile) (str)
				dataname: user desired name of the instance (str)
				version: describes the version of the instance the user is creating (default: 0) (str)

			Returns:
				string: Confirmation message

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.create_project(api,typename,dataname,version)

	def create_cutout(self,UUID,typename,dataname,version=0):
		"""
			Method to upload data onto the dvid server.

			Args:
				UUID: ID of the DVID repository where the instance is found (str)
				typename: type of data accepted by the project space (str)
				dataname: user assigned name of the project space (str)
				version: describes the version of the instance the user is creating (default: 0) (str)
				fileDir: direcotry to the file of png to upload (str)

			Returns:
				string: Confirmation message

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidResource.create_cutout(api,UUID,typename,dataname,version)

	def get_info(self, UUID):
		"""
			Method to obtain information on the requested repository

			Args:
				UUID: UUID of the DVID repository (str)

			Returns:
				string: History information of the repository

			Raises:
				(KeyError): if given invalid version.
		"""
		return DvidService.get_info(api,UUID)

	def get_log(self, UUID):
		"""
		Method to obtain log of all previous messages related to the repository

		Args:
		    UUID: UUID of the DVID repository (str)

		Returns:
		    string: list of all log recordings related to the DVID repository

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.get_log(api,UUID)

	def post_log(self, UUID,log1):
		"""
		Method to post new log information to the repository 

		Args:
		    UUID: UUID of the DVID repository (str)
		    log1: Message to record on the repositories history log (str)

		Returns:
		    string: Confirmation message

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.post_log(api,UUID,log1)

	def get_server_info(self):
		"""
		Method to obtain information about the server

		Args:
		    none

		Returns:
		    string: Server information

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.get_server_info(api)

	def change_server_setting(self,gc1,throt1):
		"""
		NOT IMPLEMENTED
		Method to change the server settings

		Args:
		    version (string): Version of Boss API to use.

		Returns:
		    None

		Raises:
		    (KeyError): if given invalid version.
		"""
		return DvidService.change_server_setting(api,gc1,throt1)
		