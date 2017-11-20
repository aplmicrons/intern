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


class DicedRemote(Remote):

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


	def get_cutout(self, IDrepos, xspan, yspan, zspan):
		"""
			Method to obtain requested array within diced server

			Args:
				ID (string): UUID assigned to DVID repository
				repos (string): name of the repository assigned by the user when instance was created

			Returns:
				(String touple)

			Raises:
				(KeyError): if given invalid version.
		"""
		return DicedResource.get_cutout(ID,repos)


	def create_cutout(self,name,array1,xs,ys,zs,typea="ArrayDtype.uint16"):
		"""
			Method to create an array inside the diced repository

			Args:
				name (string): name of the array the user wants to assign
				type(stirng): type of array (defaut = ArrayDtype.uint16)
				array1(array): numpy array to upload
				xs(int) : starting x point within server
				ys(int) : starting y point within server
				zs(int) : starting z point within server
			Reuturns:

		"""
		return DicedResource.create_cutout(name,typea,array1,xs,ys,zs)
