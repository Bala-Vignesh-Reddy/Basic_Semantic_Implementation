import numpy as np
from transformers import CLIPProcessor, CLIPModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import requests
from PIL import Image
import os
import matplotlib.pyplot as plt

image_embeddings = np.load("image_embeddings.npy")
image_dir = "./images/"
image_embeddings = np.squeeze(image_embeddings, axis=1)
print("Image Embedding shape:", image_embeddings.shape)

if image_embeddings.shape[1] != 512:
    raise ValueError(f"Unexpected embedding size: {image_embeddings.shape[1]}, expected 512")

# UNCOMMENT THIS try except BLOCK WHEN RUNNING THIS SCRIPT
# try:
#     model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
#     processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
#     print("model loaded")
# except Exception as e:
#     print("Error loading model:", e)


def get_query_embedding(query, processor, model):
    inputs = processor(text=query, return_tensors="pt", padding=True)
    query_embedding = model.get_text_features(**inputs)
    print("query embedding shape:", query_embedding.shape)
    query_embedding = query_embedding.detach().numpy()
    print("query embedding shape after detach and numpy:", query_embedding.shape)
    query_embedding = query_embedding.reshape(1,-1)
    
    return query_embedding

def semantic_search(query, image_embeddings, processor, model, top_k=5):
    query_embedding = get_query_embedding(query, processor, model)
    print("query embedding shape before cosine similarity:", query_embedding.shape)
    # similarities = cosine_similarity(query_embedding.detach().numpy(), image_embeddings)
    similarities = cosine_similarity(query_embedding, image_embeddings)

    top_k_indices = similarities[0].argsort()[-top_k:][::-1]

    return top_k_indices

def display_results(top_k_indices, image_dir):
    plt.figure(figsize=(15, 5))
    for idx, img_idx in enumerate(top_k_indices):
        img_path = os.path.join(image_dir, f"image_{img_idx}.jpg")  
        if os.path.exists(img_path):
            img = Image.open(img_path)
            plt.subplot(1, len(top_k_indices), idx + 1)
            plt.imshow(img)
            plt.axis("off")
            plt.title(f"Image {idx+1}")
    plt.show()

if __name__ == "__main__":
    while True:
        query = input("Enter query (or 'q' to exit): ")
        if query.lower() == 'q':
            break
            
        top_k_indices = semantic_search(query, image_embeddings, processor, model)
        print(f"Top {len(top_k_indices)} similar images indices: {top_k_indices}")
        display_results(top_k_indices, image_dir)