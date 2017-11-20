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
from intern.resource.localFile.resource import *
# from intern.service.localFile.service import *

LATEST_VERSION = 'v0'
host = 'filePath'


class LocalRemote(Remote):

	def __init__(self, specs, version=None):
		"""
			Constructor:
			Checks for latest version. If no version is given, assigns version as none
			Protocol and host specifications are taken in as keys -values of dictionary.
			global api variable is named and used for every command that requires api.
		"""

		if version is None:
			version = LATEST_VERSION

		path = specs[host]

		global filePath
		filePath = path

	def create_LocalFile(self,filePath):
		"""

		"""
		return LocalResource.create_LocalFile(filePath)


	def get_cutout(self, IDrepos, xspan, yspan, zspan):
		"""
			Method to request a volume of data from dvid server

			Args:
				IDrepos (string) : UUID assigned to DVID repository and repository name
				xspan (int) : range of pixels in x axis ([1000:1500])
				yspan (int) : range of pixels in y axis ([1000:1500])
				zspan (int) : range of pixels in z axis ([1000:1010])

			Returns:
				array: numpy array representation of the requested volume

			Raises:
				(KeyError): if given invalid version.
		"""
		return LocalResource.get_cutout(api,IDrepos,xspan,yspan,zspan)


	def create_project(self, filePath, groupName, subGroup):
		"""
			Method to create a project space in the dvid server

			Args:
				typename (string): describes data type stored (labelblk, labelvol, imagetile)
				dataname (string): user desired name of the instance
				version (int): describes the version of the instance the user is creating (default: 0)

			Returns:
				string: Confirmation message

			Raises:
				(KeyError): if given invalid version.
		"""
		return LocalResource.create_project(filePath, groupName, subGroup)

	def create_cutout(self, subGroup, dataArray):
		"""
			Method to upload data onto the dvid server.

			Args:
				UUID (string): ID of the DVID repository where the instance is found
				typename (string): type of data accepted by the project space
				dataname (string): user assigned name of the project space
				version (string): describes the version of the instance the user is creating (default: 0)
				fileDir (string): direcotry to the file of png to upload

			Returns:
				string: Confirmation message

			Raises:
				(KeyError): if given invalid version.
		"""
		return LocalResource.create_cutout(subGroup, dataArray)
