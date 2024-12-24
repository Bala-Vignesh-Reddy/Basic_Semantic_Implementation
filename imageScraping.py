import requests
import os
from dotenv import load_dotenv

load_dotenv()
ACESS_KEY = os.getenv('ACCESS_KEY')
SAVE_DIR = "./images/"
base_url = "https://api.unsplash.com/"

def fecth_images(queries):
    count=5
    for query in queries:
        # url = f"{base_url}photos/random?={query}&count={count}&client_id={ACESS_KEY}"
        url = f"{base_url}/search/photos?query={query}&per_page={count}&client_id={ACESS_KEY}"
        # url = "https://www.istockphoto.com/search/2/image?family=creative&phrase=hoddie"
        response = requests.get(url)
        # print(response)
        
        if response.status_code == 200:
            data = response.json()
            if "results" in data:
                if not os.path.exists(SAVE_DIR):
                    os.makedirs(SAVE_DIR)
                
                for idx, photo in enumerate(data["results"]):
                    # print(photo) 
                    img_url = photo["urls"]["regular"]
                    img_data = requests.get(img_url).content
                    img_filename = f"{query}_{idx + 1}.jpg"
                    img_path = os.path.join(SAVE_DIR, img_filename)
                    with open(img_path, "wb") as img_file:
                        img_file.write(img_data)
                print(f"Downloaded {count} images to {SAVE_DIR}")
            else:
                print("No results foundi n response")
        else:
            print("failed to fetch images")


query = ["beach", "mountain", "plains", "india", "gujarat", "usa", "london", "paris", "dubai", "building", "food", "fruit", "vegetables", "pizza", "basketball", "football", "cricket", "nature", "travel", "animals", "tamil-nadu", "arts-culture", "people", "health", "wallpapers"]
fecth_images(query)