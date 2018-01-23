import intern
from intern.remote.localFile import LocalRemote
from intern.remote.boss import BossRemote
from intern.resource.boss.resource import ChannelResource
import matplotlib.pyplot as plt
import numpy as np

# BOSS Data fetch which we will upload to the Local Storage:
boss = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88",
})
volumeB = boss.get_cutout(
    boss.get_channel("em", "pinky40", "v7"), 1,
    [10000, 10200], [10000, 10090], [500, 520],
)

#First start remote with path to be adressed and datastore name
#If the datastore name does not exist in the specified path, it will be create_dataset
#otherwise you may continue.
local = LocalRemote({
    "host": "/Users/rodrilm2/InternRel/",
    "datastore":"LocalBossDummy"
    })

#Creating a collection and channel to store the data within the local datastore
Collection1 = local.create_collection('pinky2')
Channel11 = local.create_channel(Collection1,'em2')
#The actual volume of data to be uploaded to the desired channel
volume = local.create_cutout(Channel11,'v1',volumeB)

#To download the data you can use the get_cutout function just as in the boss remote
volumeL = local.get_cutout(
    local.get_channel('pinky2', 'em2', 'v1'), 1,
    [0, 200], [0, 90], [0, 20]
)

#Showing a slice of the volume
imgplot = plt.imshow(volumeL[0,:,:])
plt.show()

#Creating a extra collection and channel for demonstration purposes
Collection2 = local.create_collection('MouseBrain2')
Collection3 = local.create_collection('FlyBrain2')
Collection4 = local.create_collection('PinkyBrain2')
Channel21 = local.create_channel(Collection2,'em')
Channel22 = local.create_channel(Collection2,'flo')
Channel31 = local.create_channel(Collection3,'fly')

#Additional possible functions
print 'This is a list of all the posible files you can access within this local datastore:'
print local.list_groups()

print 'Using local.retrieve you can get the HDF5 dataset saved on the requested path:'
print local.retrieve('pinky2/em2/v1')
