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
    "datastore":"LocalBossDummy"
    })
Collection1 = local.create_collection('pinky2')
Channel11 = local.create_channel(Collection1,'em2')
volume = local.create_cutout(Channel11,'v1',volumeB)

#LocalMetadata


#Local to Boss upload of annotated data
Collection1 = boss.create_collection('pinky2')
Channel11 = boss.create_channel(Collection1,'em2')
volume = boss.create_cutout(Channel11,'v1',volumeB)
