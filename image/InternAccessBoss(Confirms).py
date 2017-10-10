from intern.remote.boss import BossRemote
import matplotlib.pyplot as plt
from PIL import Image


#Before you begin make sure you have done the following:
	# Through your terminal or cmd travel to the directory where you have saved intern
	# git init
	# git checkout integration
	# git status and make sure you are inside the integration branch
	# git pull
	# pip install -U .
#You are ready! 
#If you would like to get multiple images you can make a while loop or for loop, let me know
#if you want me to do it :)

boss = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    #Remember to change your token here. You can get your own at: https://api.theboss.io/token/
    "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88"
})

#Here you will specify form where the data is coming from, the resolution, and the size of your image.
volume = boss.get_cutout(
    boss.get_channel("cc", "kasthuri2015", "em"), 0,
    [5000, 6000], [8000, 9000], [1100, 1200],
)

volume2 = boss.get_cutout(
    boss.get_channel("mitochondria", "kasthuri2015", "em"), 0,
    [5000, 6000], [8000, 9000], [1100, 1200],
)

volume3 = boss.get_cutout(
    boss.get_channel("3cylsynapse_v1", "kasthuri2015", "em"), 0,
    [5000, 6000], [8000, 9000], [1100, 1200],
)

volume4 = boss.get_cutout(
    boss.get_channel("3cylneuron_v1", "kasthuri2015", "em"), 0,
    [5000, 6000], [8000, 9000], [1100, 1200],
)

#We can print all the volume variables. This is most likely what you will need to 
#analyze the data. So you would use the volume variables as you wish. Remember these are saved as
#numpy arrays!
print(volume)
print(volume2)
print(volume3)
print(volume4)

#This will show the figures that will pop up once the program is done running
#Each figure corresponds to a different annotation
fig1 = plt.figure(1)
plt.imshow(volume[1,:,:])
fig2 = plt.figure(2)
plt.imshow(volume2[1,:,:])
fig3 = plt.figure(3)
plt.imshow(volume3[1,:,:])
fig4 = plt.figure(4)
plt.imshow(volume4[1,:,:])

#This will save all the figures created above, which we will then use to overlay. 
fig1.savefig("cc.png")
fig2.savefig("mit.png")
fig3.savefig("syn.png")
fig4.savefig("neu.png")

#Blending all the images requires we assign a variable to each image.
background = Image.open("cc.png")
overlay1 = Image.open("mit.png")
overlay2 = Image.open("syn.png")
overlay3 = Image.open("neu.png")

#This will blend all the images together.
new_img = Image.blend(background, overlay1, 0.5)
new_img2 = Image.blend(new_img, overlay2, 0.5)
new_img3 = Image.blend(new_img2, overlay3, 0.5)

#Saves the blended images to your current directory.
new_img3.save("OverlayImage.png", "PNG")

#Will open your overlayed image and show it.
overlay = Image.open("OverlayImage.png")
overlay.show()

#Here just to show the individual  figures if you want them.
plt.show()