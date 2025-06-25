from duckduckgo_search import DDGS
import requests
import os

# Parameters
search_query = "fridge with food items inside"
output_dir = "fridge_images"
num_images = 1000  # Number of images to download

# Create folder if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Search and download
with DDGS() as ddgs:
    results = ddgs.images(search_query, max_results=num_images)
    print(f"Found {len(results)} images. Downloading...")

    for idx, result in enumerate(results):
        image_url = result['image']
        try:
            img_data = requests.get(image_url, timeout=10).content
            file_name = os.path.join(output_dir, f"fridge_{idx + 1}.jpg")
            with open(file_name, 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded: {file_name}")
        except Exception as e:
            print(f"Failed to download image {idx + 1}: {e}")

print("Download complete.")
