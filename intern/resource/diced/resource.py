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

    """Base class for Dvid resources.

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
    def get_cutout(self, api, IDrepos, xspan, yspan, zspan):

        """
            ID MUST BE STRING ""
            xpix = "x" how many pixels traveled in x
            ypix = "y" how many pixels traveled in y
            zpix = "z" how many pixels traveled in z
            xo, yo, zo (x,y,z offsets)
            type = "raw"
            scale = "grayscale"
        """

        #Returns a 3-dimensional numpy array to the user
        return entire_space2

    @classmethod
    def create_cutout(self, api, UUID, dataname, volume, x, y, z, x0, y0,z0 , version=0):

        """
            Creates an instance which works as a sub-folder where the data is stored
            Must specify:
            dataname(required) = "example1"
            version(required) = "1"
            The size of the space reserved must be a cube with sides of multiples of 32
        """

        return(res.content)
