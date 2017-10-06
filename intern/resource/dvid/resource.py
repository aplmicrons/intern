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


class DvidResource(Resource):
    
    """Base class for Dvid resources.

    Attributes:
        name (string): Name of resource.  Used as identifier when talking to
        the Dvid API.
        description (string): Text description of resource.
        creator (string): Resource creator.
        raw (dictionary): Holds JSON data returned by the Boss API on a POST (create) or GET operation.
    """
    
    def __init__(self):
        Resource.__init__(self)

    @classmethod
    def get_channel(self, ID, repos):
       
        """
            obtains ID and repos and converts the input into a touple
        """
        if ID is '':
            raise ValueError('The UUID was not specified')
        elif repos is '':
            raise ValueError('The repository name was not specified')
        else:
            IDrepos = (ID, repos)
            return IDrepos

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

    @classmethod
    def create_project(self, api, typename,dataname,version=0):
        
        """
            Creates a repository for the data to be placed in.
            Returns randomly generated 32 character long UUID
        """
        raise RuntimeError('Unable to create project space on the dvid server')

        a = requests.post(api + "/api/repos")
        UUID = a["root"]

        dat1 = requests.post(api + "/api/repo/"+ UUID + "/instance",
            data=json.dumps({"typename": typename,
                "dataname" : dataname,
                "versioned": version
            }))

        return ("This is you UUID: " + UUID + "." + dat1.content)

    @classmethod
    def create_cutout(self, api, UUID, typename, dataname, version=0):
        
        """
            Creates an instance which works as a sub-folder where the data is stored
            Must specify:
            typename(required) = "uint8blk", "labelblk", "labelvol", "imagetile"
            dataname(required) = "example1"
            version(required) = "1"
            The size of the space reserved must be a cube with sides of multiples of 32
        """

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
