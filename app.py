import streamlit as st
from PIL import Image
from search import semantic_search
import numpy as np
from transformers import CLIPModel, CLIPProcessor 
import os

os.environ["STREAMLIT_SUPPRESS_RUN_CONTEXT_WARNING"] = "1"

image_embeddings = np.load("image_embeddings.npy") # this is in 3d model
image_embeddings = np.squeeze(image_embeddings, axis=1) # this is in 2d model

try:
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    print("model loaded")
except Exception as e:
    print("Error loading model:", e)

# st.write("I have downloaded 125 images from unsplash images.. there are certain categories which i have downloaded.. but similarly we can do it for large number of images..")
st.title("Semantic Image Search")
st.subheader("Images are locally stored.. this is done to display images")
st.write("Categories are: beach, mountain, plains, india, gujarat, usa, london, paris, dubai, building, food, fruit, vegetables, pizza, basketball, football, cricket, nature, travel, animals, tamil-nadu, arts-culture, people, health, wallpapers")
query = st.text_input("Search for images:")

IMAGE_DIR="./images/"
if query:
    results = semantic_search(query, image_embeddings, processor, model, top_k=4)
    st.write("Search Results:")
    col1, col2 = st.columns(2)
    
    for i, img_name in enumerate(results):
        img_path = os.path.join(IMAGE_DIR, f"image_{img_name}.jpg")
        try:
            img = Image.open(img_path)
            img = img.resize((200, 200))
            if i % 2 == 0:  
                with col1:
                    st.image(img, use_container_width=True)
            else:  
                with col2:
                    st.image(img, use_container_width=True)
 


        except FileNotFoundError:
            st.error(f"Image not found: {img_path}")
        except Exception as e:
            st.error(f"Error loading image {img_path}: {str(e)}")

