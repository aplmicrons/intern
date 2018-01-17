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
from intern.resource.diced.resource import *

class DicedRemote(Remote):

	def __init__(self, specs, version=None):
		"""
			Constructor.

			Checks for latest version. If no version is given, assigns version as none
			Protocol and host specifications are taken in as keys -values of dictionary.
			global api variable is named and used for every command that requires api.
		"""

	def get_cutout(self, dicedName, idRepos,arrayName, xspan, yspan, zspan):
		"""
			Method to request a volume of data from dvid server

			Args:
                reposName (str) : Name of the local DICED repository
                IDrepos (str) : UUID assigned to DICED repository and repository name
                arrayName (str) : Name of the specific array desired
                xspan (int) : range of pixels in x axis ([1000:1500])
				yspan (int) : range of pixels in y axis ([1000:1500])
				zspan (int) : range of pixels in z axis ([1000:1010])

			Returns:
				array: numpy array representation of the requested volume

			Raises:
				(KeyError): if given invalid version.
        """
		return DicedResource.get_cutout(dicedName, idRepos,arrayName, xspan, yspan, zspan)


	def create_cutout(self,dicedName, idRepos,arrayName,array1,xs,ys,zs,typea="ArrayDtype.uint16"):
		"""
			Method to create an array inside the diced repository

			Args:
		        dicedName (str): Name of DICED file
		        idRepos (str) : name of repository within DICED
		        arrayName(str) : Desired Array name
		        typea(str): type of array (defaut = ArrayDtype.uint16)
				xs(int) : starting x point within server
				ys(int) : starting y point within server
				zs(int) : starting z point within server
			Reuturns:

		"""

		return DicedResource.create_cutout(dicedName, idRepos,arrayName, typea, array1,xs,ys,zs)
