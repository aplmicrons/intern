from intern.remote.boss import BossRemote
from intern.resource.boss.resource import *
import numpy

rmt = BossRemote({
    "protocol": "https",
    "host": "api.theboss.io",
    "token": "db1cec2c865fc84e48772f4f4a5f010c0a180b88"
})

COLL_NAME = 'Data_Acc_t17'
EXP_NAME = 'Luis_test'
CHAN_NAME = 'one'
DATA_BASE = 'large'

# Create a new channel that uses uint16 data.
chan_setup = ChannelResource(CHAN_NAME, COLL_NAME, 
	EXP_NAME,'image', datatype='uint16')
chan = rmt.create_project(chan_setup)

# Upload the cutout to the channel.  The zero parameter specifies native
# resolution.
rmt.create_cutout(chan, 0, x_rng, y_rng, z_rng, data)

# Ranges use the Python convention where the second number is the stop
# value.  Thus, x_rng specifies x values where: 0 <= x < 8.
x_rng = [0, 8]
y_rng = [0, 4]
z_rng = [0, 5]

# Note that the numpy matrix is in Z, Y, X order.
data = numpy.random.randint(0, 3000, (5, 4, 8))
# Make data match what was specified for the channel.
data = data.astype(numpy.uint16)