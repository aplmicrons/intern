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
    def create_project(self, filePath, fileName, groupName, subGroup):

        """
            Creates a repository for the data to be placed in.
            Returns randomly generated 32 character long UUID
        """
        groupPath = str(filePath) + str(fileName)
        f = h5py.File(groupPath, 'w')
        grp = f.create_group(groupName)
        subgrp = grp.create_group(subGroup)

        return (subgrp)

    @classmethod
    def create_cutout(self, subgrp, dataArray):

        """
            Creates an instance which works as a sub-folder where the data is stored
            Must specify:
            dataname(required) = "example1"
            version(required) = "1"
            The size of the space reserved must be a cube with sides of multiples of 32
        """
        dset = subgrp.create_dataset("autochunk", data = dataArray)

        return(dset)

    @classmethod
    def get_cutout(self, filePath, group, subGroup, xspan, yspan, zspan):

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

        return entire_space2

# import numpy as np
# import intern
# from intern.remote.localFile import LocalRemote
# from intern.remote.boss import BossRemote
# from intern.resource.boss.resource import ChannelResource

# # filePath = "tomorrow/today/"
# # fileName = "LoalTest"
# # form = ".hdf5"
# # dirP = filePath + fileName + form
# #
# # print(dirP)
#
# # BOSS Data fetch:
# boss = BossRemote({
#     "protocol": "https",
#     "host": "api.theboss.io",
#     "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88",
# })
# volumeB = boss.get_cutout(
#     boss.get_channel("em", "pinky40", "v7"), 1,
#     [10000, 10500], [10000, 10500], [500, 501],
# )
# local = LocalRemote({
#     "host" : "~/Users/rodrilm2/"
# })
#
# locFil = local.create_LocalFile("LocalTest")
# # locProj = locFil.create_project("TestGroup", "BossLocalData")
#
# # dset = local.create_cutout(locProj, volumeB)
#
# # print(dset)
