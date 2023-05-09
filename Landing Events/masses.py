import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.colors as mcolors

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
contrasts_norm = contrast / np.max(contrast)

# Filter data with mass >= 0 and mass <= 300
valid_masses = (masses_kDa >= 0) & (masses_kDa <= 300)

x_coords = x_coords[valid_masses]
y_coords = y_coords[valid_masses]
frame_indices = frame_indices[valid_masses]  # Add this line to filter frame_indices
masses_kDa = masses_kDa[valid_masses]
contrast = contrast[valid_masses]

# Find the minimum and maximum mass values
min_mass = np.min(masses_kDa)
max_mass = np.max(masses_kDa)

# Normalize and scale masses for size
size_scale = 50
if max_mass == min_mass:
    masses_norm = np.zeros_like(masses_kDa)
else:
    masses_norm = (masses_kDa - min_mass) / (max_mass - min_mass)
sizes = masses_norm * size_scale + 10

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = plt.scatter(x_coords, y_coords, c=masses_kDa, s=sizes, cmap='viridis', alpha=0.6)

# Set colorbar
cbar = plt.colorbar()
cbar.set_label('Mass (kDa)')

# Set the color of each data point based on contrast
face_colors = [plt.cm.binary(txt) for txt in contrast / np.max(contrast)]
scatter_plot.set_facecolors(face_colors)

plt.xlabel('Length (nm)')
plt.ylabel('Height (nm)')
plt.title('Mass Photometry Distribution')
plt.tight_layout()
plt.savefig("mass_photometry.png")
plt.show()

