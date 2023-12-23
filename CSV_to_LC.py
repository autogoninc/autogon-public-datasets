import pandas as pd
from PIL import Image
import os

# Load the CSV data
data = pd.read_csv("BBox_List_2017.csv")

# Create the 'labels' directory if it doesn't exist
os.makedirs("labels", exist_ok=True)

# Get unique label names and create a list
unique_labels = list(data["label"].unique())

# Create a dictionary to map label names to their indices
label_to_index = {label: i for i, label in enumerate(unique_labels)}

# Iterate through each row in the CSV
for index, row in data.iterrows():
    image_name = row["Image Index"]
    label = row["Finding Label"]
    x = row["Bbox [x"]
    y = row["y"]
    w = row["w"]
    h = row["h]"]

    # Get the label index
    label_index = label_to_index[label]

    # Load the image using PIL to get its dimensions
    image = Image.open(os.path.join("images", image_name))
    image_width, image_height = image.size

    # Convert bounding box coordinates to YOLO format (normalized coordinates)
    x_center = (x + w / 2) / image_width
    y_center = (y + h / 2) / image_height
    width_normalized = w / image_width
    height_normalized = h / image_height

    # Create the label text in YOLO format using the label index
    label_text = (
        f"{label_index} {x_center} {y_center} {width_normalized} {height_normalized}\n"
    )

    # Write the label text to a file in the 'labels' directory
    with open(
        os.path.join("labels", os.path.splitext(image_name)[0] + ".txt"), "a"
    ) as f:
        f.write(label_text)

print("Label files created successfully!")
print("Unique label names:", unique_labels)
