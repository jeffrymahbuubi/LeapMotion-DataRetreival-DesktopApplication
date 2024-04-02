import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


# Function to plot a single bone with markers for joints
def plot_bone_with_markers(ax, start_x, start_y, start_z, end_x, end_y, end_z, color):
    # Plotting the bone
    ax.plot([start_x, end_x], [start_y, end_y], [start_z, end_z], color=color)
    # Adding marker for the start joint
    ax.scatter(start_x, start_y, start_z, color=color, marker="o")
    # Adding marker for the end joint
    ax.scatter(end_x, end_y, end_z, color=color, marker="o")


# Load your data here
file_path = "test2.xlsx"  # Update with your actual file path
data = pd.read_excel(file_path)

# Setting up the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Define colors for each finger for better distinction
finger_colors = {"thumb": "r", "index": "g", "middle": "b", "ring": "y", "pinky": "m"}

# Iterate through each row in the dataframe to plot each bone with markers
for index, row in data.iterrows():
    for finger, color in finger_colors.items():
        start_x = row[f"{finger}_start_x_device_1"]
        start_y = row[f"{finger}_start_y_device_1"]
        start_z = row[f"{finger}_start_z_device_1"]
        end_x = row[f"{finger}_end_x_device_1"]
        end_y = row[f"{finger}_end_y_device_1"]
        end_z = row[f"{finger}_end_z_device_1"]

        plot_bone_with_markers(
            ax, start_x, start_y, start_z, end_x, end_y, end_z, color
        )

# Setting labels for better understanding
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
ax.set_title(
    "3D Visualization of Hand Structure with Joint Markers from Leap Motion Data"
)

# Show plot with markers
plt.show()
