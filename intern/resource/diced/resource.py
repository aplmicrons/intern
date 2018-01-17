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

from intern.resource import Resource
from abc import abstractmethod
from io import BytesIO
import numpy as np
import requests
import json
from diced import DicedStore, ArrayDtype

class DicedResource(Resource):

    """Base class for Diced resources.

    Attributes:
        name (string): Name of resource.  Used as identifier when talking to
        the Dvid API.
        description (string): Text description of resource.
        creator (string): Resource creator.
        raw (dictionary): Holds JSON data returned by DVID on a POST (create) or GET operation.
    """

    def __init__(self):
        """
            Initializes intern.Resource parent class
        """
        Resource.__init__(self)


    @classmethod
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

                store = DicedStore(dicedName)
                repo = store.open_repo(idRepos)
                my_array = repo.get_array(arrayName)

                return my_array


    @classmethod
    def create_cutout(self,dicedName, idRepos,arrayName, typea, array1,xs,ys,zs):
        """
            Method to create an array inside the diced repository

        Args:
            dicedName (str): Name of DICED file
            idRepos (str) : name of repository within DICED
            arrayName(str) : Desired Array name
            typea(str): type of array (defaut = ArrayDtype.uint16)
            array1(array): numpy array to upload
            xs(int) : starting x point within server
            ys(int) : starting y point within server
            zs(int) : starting z point within server
        Returns:

        """
        #Array specifications to make space on server
        r1 = array1.shape[0]
        r2 = array1.shape[1]
        r3 = array1.shape[2]

        store = DicedStore(dicedName)
        repo = store.create_repo(idRepos)
        repo = store.open_repo(idRepos)
        arr = repo.create_array(arrayName,typea)
        arr[xs:r1,ys:r2,zs:r3] = np.array([array1])

        #Returns a 3-dimensional numpy array to the user
        return("Your array has been uploaded to DICED server: " + dicedName + " under repository: " + idRepos + " and name: " + arrayName)
