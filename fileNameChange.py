import os

image_dir = "./images/"

for i, filename in enumerate(os.listdir(image_dir)):
    os.rename(os.path.join(image_dir, filename), os.path.join(image_dir, f"image_{i}.jpg"))

print("File names have been changed successfully.")

