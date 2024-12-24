import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os
import numpy

try:
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    print("model loaded")
except:
    print("Error loading model")
    
IMAGE_DIR = "./images/"
embeddings = []

for img_name in os.listdir(IMAGE_DIR):
    img_path = os.path.join(IMAGE_DIR, img_name)
    image = Image.open(img_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.get_image_features(**inputs)
    embeddings.append(outputs.detach().numpy())

print(embeddings)
numpy.save("image_embeddings.npy", embeddings)