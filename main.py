import netCDF4 as nc
from PIL import Image
import numpy as np
from sklearn.preprocessing import normalize

# Import the data set
filename = "raw_data.nc"
dataset = nc.Dataset(filename)
temperature = dataset.variables['thetao']


"""
The dataset

The data set is structured in 3 dimensions: Latitude, Longitude, and Time.
For each point in time you have a 2D grid of temperature values.
"""

# Grab the 2D grid belonging to the first data point
# To grab all values in a specific dimension, use [:] for that dimension
zerotime = temperature[0,:,:] 

# Zerotime is a masked array (no idea what that is) so we convert it to normal python lists
zerotime_list = zerotime.tolist()

# The data has values of 'none' if the longitude/latitude point is on land.
# Set those values to 0 so we can plot it in an image
for i in range(len(zerotime_list)):
    for j in range(len(zerotime_list[i])):
        if zerotime_list[i][j] == None:
            zerotime_list[i][j] = 0

# Currently values are from 0 upto 15 orso, change that to 0-1 range
zerotime_normalized = normalize(zerotime_list)

# The image was flipped for some reason so we flip it back
flipped = np.flip(zerotime_normalized, 0)

img = Image.fromarray(np.uint8(flipped*255))

img.show()