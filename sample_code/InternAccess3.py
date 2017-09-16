from intern.remote.boss import BossRemote
from intern.resource.boss.resource import ChannelResource
import matplotlib.pyplot as plt
import numpy as np
# from stl import mesh

boss = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88"
})

#Here you will specify form where the data is coming from, the resolution, and the size of your image.
volume = boss.get_cutout(
    boss.get_channel("em", "pinky40", "v7"), 1,
    [10000, 10500], [10000, 10500], [500, 550],
)

# volume = array_map('floatval',nonFloats)
# print(volume)
np.set_printoptions(threshold='nan')
print(volume)
# plt.imshow(volume[1,:,:])

# plt.show()

# vertices = np.array([\
#     [-1, -1, -1],
#     [+1, -1, -1],
#     [+1, +1, -1],
#     [-1, +1, -1],
#     [-1, -1, +1],
#     [+1, -1, +1],
#     [+1, +1, +1],
#     [-1, +1, +1]])

# cube = mesh.Mesh(np.zeros(volume.shape[0], dtype = mesh.Mesh.dtype))
# for i, f in enumerate(volume):
# 	for j in range(3):
# 		cube.vectors[i][j] = vertices[f[j],:]
# cube.save('cube.stl')