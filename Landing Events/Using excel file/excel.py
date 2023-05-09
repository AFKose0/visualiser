import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.lines import Line2D
import pandas as pd

# Load the data from xlsx file
data = pd.read_excel("Landing events.xlsx")

# Clean the data by removing non-numeric rows
data = data[data['frame_indices'].apply(lambda x: isinstance(x, (int, float)))]

# Extract columns as NumPy arrays
x_coords = data['x_coords'].to_numpy()
y_coords = data['y_coords'].to_numpy()
frame_indices = data['frame_indices'].to_numpy(dtype=float)
masses_kDa = data['masses_kDa'].to_numpy()
contrast = data['contrasts'].to_numpy()

# Process the data
coords = list(zip(x_coords, y_coords))
coord_counts = defaultdict(int)

for coord in coords:
    coord_counts[coord] += 1

overlap_colors = frame_indices
size_scale = masses_kDa / np.min(masses_kDa) * 100
contrasts_norm = contrast / np.max(contrast)

# Create the scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = plt.scatter(x_coords, y_coords, c=overlap_colors, s=size_scale, cmap='viridis', alpha=0.6)

# Set colorbar
cbar = plt.colorbar()
cbar.set_label('Time (seconds)')

# Create a mass scale legend
mass_scale_values = np.array([0, 50, 100, 150, 200, 250, 300])  # Updated mass values
mass_scale_sizes = mass_scale_values / np.min(mass_scale_values[1:]) * 100  # Updated size calculation to avoid dividing by zero

handles = []
labels = []
for mass, size in zip(mass_scale_values, mass_scale_sizes):
    marker = Line2D([0], [0], linestyle='none', marker='o', markersize=np.sqrt(size), color='black', alpha=0.6)  # Use Line2D and square root of size
    handles.append(marker)
    labels.append(f'{mass:.1f} kDa')

legend2 = plt.legend(handles, labels, title='Mass Scale', loc='upper left', bbox_to_anchor=(1.2, 1.0), borderaxespad=0)

plt.xlabel('X-Coordinate')
plt.ylabel('Y-Coordinate')
plt.title('Mass Photometry Results')
plt.tight_layout()
plt.savefig("mass_photometry_results.png", bbox_extra_artists=(legend2,), bbox_inches='tight')
plt.show()
