import pandas as pd
import matplotlib.pyplot as plt

# Read data from the files
frame_indices = pd.read_csv("frame_indices.txt", header=None, names=["frame"])
masses_kDa = pd.read_csv("masses_kDa.txt", header=None, names=["mass"])
contrasts = pd.read_csv("contrasts.txt", header=None, names=["contrast"])

# Combine the data into a single DataFrame
data = pd.concat([frame_indices, masses_kDa, contrasts], axis=1)

# Filter data based on mass values
filtered_data = data[(data["mass"] <= 250) & (data["mass"] >= -250)].copy()

# Convert frame numbers to time (subtract 1 from frame number to account for 0-based index)
filtered_data.loc[:, "time"] = (filtered_data["frame"] - 1) / 60

# Plot the distribution
plt.figure(figsize=(8, 4))
scatter = plt.scatter(filtered_data["time"], filtered_data["mass"], c=filtered_data["contrast"], cmap="viridis", alpha=0.5)
plt.colorbar(scatter, label="Contrast", orientation="horizontal")
plt.xlabel("Time (s)")
plt.ylabel("Mass (kDa)")
plt.title("Filtered Mass Photometry Results")
plt.show()
