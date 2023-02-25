import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# load x and y coordinates from text files
x_coords = [float(x) for x in open("x_coords.txt")]
y_coords = [float(y) for y in open("y_coords.txt")]

# create figure and axis objects
fig, ax = plt.subplots()

# create scatter plot
scatter = ax.scatter(x_coords, y_coords)

# load frame indices from text file
with open("frame_indices.txt") as f:
    frame_indices = [int(i.strip()) for i in f]

# create horizontal slider
ax_slider = plt.axes([0.1, 0.05, 0.8, 0.1])
slider = Slider(ax_slider, "Frames", min(frame_indices), max(frame_indices), valinit=min(frame_indices), valstep=60)

# update plot when slider value is changed
def update(val):
    # get new frame index from slider value
    frame_index = int(slider.val)

    # update x and y coordinates for scatter plot
    scatter.set_offsets(np.c_[x_coords[frame_index], y_coords[frame_index]])

# connect update function to slider
slider.on_changed(update)

# show plot
plt.show()
