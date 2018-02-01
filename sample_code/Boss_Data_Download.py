from intern.remote.boss import BossRemote
from intern.resource.boss.resource import ChannelResource
import matplotlib.pyplot as plt
import numpy as np

boss = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88"
})

#Here you will specify form where the data is coming from, the resolution, and the size of your image.
volume = boss.get_cutout(
    boss.get_channel("em", "pinky40", "v7"), 0,
    [10000, 10500], [10000, 10500], [500, 550],)

print(volume)
plt.imshow(volume[1,:,:], cmap= "gray")
plt.show()
