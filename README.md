# Semantic Search (Text to Image)

This is a simple streamlit application that allows us to search for images based on text query.. the images are scraped from unsplash images.. certain categories are choosed and downloaded.. 125 images are installed locally.. 

then using Open AI's CLIP model is used to generate embeddings for the downlaoded images.. and it is stored in a numpy array.. locally, then model is loaded and scikit-learn's cosine similarity is used to find the most nearest embeddings for the given query..

Similarly, we can implement this for large number of images.. where we have to store the embeddings in vector database and perform search.. and implement different types of search like image to image, image to text, hybrid search etc..

## Installtion (setting up for streamlit)

```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```
 
## To run it locally.. run the search.py file.. (uncomment the try except block in file before executing)
```bash 
python search.py
```

# Conclusion
This is the first step towards semantic search.. next would be integrating with vector database and add different types of search with large number of datasets..
