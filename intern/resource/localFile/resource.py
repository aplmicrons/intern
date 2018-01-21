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
import numpy as np
import h5py


class LocalResource(Resource):

    """Base class for LocalFile resources.

    Attributes:
        name (string): Name of resource.  Used as identifier when talking to
        the LocalFile database.
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
    def create_LocalFile(self,filePath,fileName):
        """

        """
        form = ".hdf5"
        dirP = str(filePath) + str(fileName) + str(form)
        f = h5py.File(dirP, 'w')
        return f

    @classmethod
    def create_collection(self, f, groupName):

        """
            Creates a repository for the data to be placed in.
            Returns randomly generated 32 character long UUID
        """
        grp = f.create_group(groupName)
        return (grp)

    @classmethod
    def create_channel(self, groupName, subGroup):
        """
            Creates a repository for the data to be placed in.
            Returns randomly generated 32 character long UUID
        """
        subgrp = groupName.create_group(subGroup)
        return (subgrp)

    @classmethod
    def create_cutout(self, subgrp, ArrayName, dataArray):

        """
            Creates an instance which works as a sub-folder where the data is stored
            Must specify:
            dataname(required) = "example1"
            version(required) = "1"
            The size of the space reserved must be a cube with sides of multiples of 32
        """
        dset = subgrp.create_dataset(ArrayName, data = dataArray)

        return(dset)

    @classmethod
    def get_channel(self,collection,channel,experiment):
        channelSource = str(collection + '/' + channel + '/' + experiment)
        return channelSource

    @classmethod
    def get_cutout(self, datastore, channelRes, res, xspan, yspan, zspan):

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
        print zpix, xpix,ypix
        dataLoc = datastore[channelRes]
        print dataLoc[0,:,:]
        vol = dataLoc[zo:zpix,yo:ypix,xo:xpix]
        print vol
        return vol

    @classmethod
    def retrieve(self, datastore, path):
        retrF = datastore[path]
        return retrF

    @classmethod
    def list_groups(self, userFind):
        def printname(name):
            print name
        return userFind.visit(printname)
