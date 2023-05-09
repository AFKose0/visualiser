import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# Load the data
x_coords = np.loadtxt("x_coords.txt")
y_coords = np.loadtxt("y_coords.txt")
frame_indices = np.loadtxt("frame_indices.txt", dtype=float)
masses_kDa = np.loadtxt("masses_kDa.txt")
contrast = np.loadtxt("contrasts.txt")

# Process the data
coords = list(zip(x_coords, y_coords))
coord_counts = defaultdict(int)

for coord in coords:
    coord_counts[coord] += 1

overlap_colors = [coord_counts[coord] for coord in coords]
size_scale = masses_kDa / np.min(masses_kDa) * 100
contrasts_norm = contrast / np.max(contrast)

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = plt.scatter(x_coords, y_coords, c=overlap_colors, s=size_scale, cmap='viridis', alpha=0.6)

# Set colorbar
cbar = plt.colorbar()
cbar.set_label('Number of Overlapping Data Points')

# Set the color of each data point based on contrast
face_colors = [plt.cm.gray_r(txt) for txt in contrasts_norm]
scatter_plot.set_facecolors(face_colors)

plt.xlabel('X-Coordinate')
plt.ylabel('Y-Coordinate')
plt.title('Mass Photometry Results')
plt.tight_layout()
plt.savefig("mass_photometry_results.png")
plt.show()
