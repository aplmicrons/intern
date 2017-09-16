from intern.remote.boss import BossRemote
from intern.resource.boss.resource import ChannelResource
import matplotlib.pyplot as plt

boss = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    "token": "bab0715e65bacfde06261c40d64213918a25c9ad"
    "Accept" : "JPEG Image"
})

#Here you will specify form where the data is coming from, the resolution, and the size of your image.
volume = boss.get_cutout(
    ChannelResource("em", "kasthuri2015", "3cylneuron_v1"), 1,
    [10000, 10500], [10000, 10500], [500, 550],
)

multi_slice_viewer(volume)


def multi_slice_viewer(volume):
    remove_keymap_conflicts({'j', 'k'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index])
    fig.canvas.mpl_connect('key_press_event', process_key)

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'j':
        previous_slice(ax)
    elif event.key == 'k':
        next_slice(ax)
    fig.canvas.draw()

def previous_slice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])

def next_slice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])

    #This while loop will output all images for slices (h=x) to seven if (h<=7)
	# plt.figure(h)
	# plt.imshow(volume[:,:,:], cmap="gray", interpolation="none")

# print(volume)

# plt.show()
