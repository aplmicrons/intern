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
#Local Upload
local = LocalRemote({
    "host": "/Users/rodrilm2/InternRel/",
    "datastore":"LocalBossDummy2"
    })
Collection1 = local.create_collection('pinky2')
Channel11 = local.create_channel(Collection1,'em2')
volumeL = local.create_cutout(Channel11,'v1',volumeB)

#LocalMetadata updates
coll_data = {'poc': 'Jane Doe'}
local.create_metadata(Collection1, coll_data)

exp_data = {'weight': '20g', 'diet': 'C2', 'date': '23-May-2016'}
local.create_metadata(Channel11, exp_data)

chan_data = {'channel_prep': '342', 'microscope': 'sem4'}
local.create_metadata(volumeL, chan_data)

chan_keys = local.list_metadata(layer)
print(chan_keys)

chan_new_data = {'channel_prep': '345', 'microscope': 'sem3'}
local.update_metadata(channel, chan_new_data)

local.delete_metadata(collection, ['poc'])

#Data processing can also be done here before re-upload

# #Local to Boss upload of annotated data
# chan_setup = ChannelResource('CHAN_NAME', 'COLL_NAME', 'EXP_NAME', 'image', datatype='uint16')
# chan = rmt.create_project(chan_setup)
# xspan = [0, 200]
# yspan = [0, 90]
# zspan = [0, 20]
#
# BossRemote.create_cutout(chan, 0, xspan, yspan, zspan, VolumeLMeta)
