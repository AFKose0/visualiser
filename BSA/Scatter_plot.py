import matplotlib.pyplot as plt

# Read the x and y values from the file
x, y = [], []
with open('xy.txt', 'r') as f:
    for line in f:
        values = line.strip().split()
        x.append(float(values[0]))
        y.append(float(values[1]))

# Plot the scatter graph
plt.scatter(x, y, s=1)
plt.xlabel('X-axis (μm)', fontweight='bold')
plt.ylabel('Y-axis (μm)', fontweight='bold')

# Remove the top and right black borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Make the other borders 3 times thicker
plt.gca().spines['bottom'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)

# Make tick marks 3 times thicker and longer
plt.tick_params(width=3, length=3)

# Increase the size of numbers and axis labels by 50%
plt.rcParams.update({'font.size': 18})


plt.show()
