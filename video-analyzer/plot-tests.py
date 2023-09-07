import matplotlib.pyplot as plt
import numpy as np

# Sample list of pixel colors (RGB values)
pixel_colors = [
    [255, 0, 0],   # Red
    [0, 255, 0],   # Green
    [0, 0, 255],   # Blue
    [255, 255, 0], # Yellow
]

# Extract individual color channels (R, G, B)
colors = np.array(pixel_colors) / 255.0

# Create a list of x-values (index of the list items)
x_values = list(range(len(pixel_colors)))

# Create a scatter plot
plt.scatter(x_values, [1] * len(pixel_colors), c=colors, marker='o', s=100)

# Customize the plot
plt.xticks(x_values)
plt.xlim(-1, len(pixel_colors))
plt.xlabel('Index')
plt.title('Pixel Color Values')

# Show the plot
plt.show()
# Wait for a key press to close the plot
plt.waitforbuttonpress()