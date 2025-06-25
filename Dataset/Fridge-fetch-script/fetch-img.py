# from duckduckgo_search import DDGS
# import requests
# import os

# # Parameters
# search_query = "fridge with food items inside"
# output_dir = "fridge_images"
# num_images = 1000  # Number of images to download

# # Create folder if not exists
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Search and download
# with DDGS() as ddgs:
#     results = ddgs.images(search_query, max_results=num_images)
#     print(f"Found {len(results)} images. Downloading...")

#     for idx, result in enumerate(results):
#         image_url = result['image']
#         try:
#             img_data = requests.get(image_url, timeout=10).content
#             file_name = os.path.join(output_dir, f"fridge_{idx + 1}.jpg")
#             with open(file_name, 'wb') as handler:
#                 handler.write(img_data)
#             print(f"Downloaded: {file_name}")
#         except Exception as e:
#             print(f"Failed to download image {idx + 1}: {e}")

# print("Download complete.")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import requests
# import os
# import time

# # Parameters
# search_query = "fridge with food items inside"
# output_dir = "fridge_images"
# num_images = 1000

# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# chrome_options = Options()
# # Uncomment if you want headless mode
# # chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--log-level=3')

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.get('https://www.bing.com/images')

# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys(search_query)
# search_box.submit()

# time.sleep(3)

# image_urls = set()
# scroll_pause_time = 2
# scroll_count = 0

# while len(image_urls) < num_images and scroll_count < 30:
#     thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.mimg")
#     print(f"Found {len(thumbnails)} thumbnails so far...")

#     for img in thumbnails[len(image_urls):]:
#         src = img.get_attribute('src')
#         if src and 'http' in src and src not in image_urls:
#             image_urls.add(src)
#             print(f"Collected image URL: {src}")
#             if len(image_urls) >= num_images:
#                 break

#     driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
#     time.sleep(scroll_pause_time)
#     scroll_count += 1

# driver.quit()
# print(f"Collected {len(image_urls)} image URLs. Starting download...")

# # Download images
# for idx, url in enumerate(image_urls):
#     try:
#         img_data = requests.get(url, timeout=10).content
#         file_path = os.path.join(output_dir, f"fridge_{idx + 1}.jpg")
#         with open(file_path, 'wb') as f:
#             f.write(img_data)
#         print(f"Downloaded: {file_path}")
#     except Exception as e:
#         print(f"Failed to download {url}: {e}")

# print("All downloads complete.")

import os
import requests
import praw
from urllib.parse import urlparse

# Replace these with your own Reddit API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
user_agent = 'image_downloader_script'

# Setup PRAW
reddit = praw.Reddit(
    client_id='rTKAz6V7Tz-f2ADDKCQvhQ',
    client_secret='s6PYOzUbHeT9ciEx70NBncrxMW8peQ',
    user_agent='image_downloader_script',
    username='Blue-Walrus',      # <- ADD THIS
    password='I6YJtg99'       # <- ADD THIS
)

# Subreddit and folder setup
subreddit_name = 'FridgeDetective'
download_folder = 'reddit-fridge'
os.makedirs(download_folder, exist_ok=True)

# Fetch posts
subreddit = reddit.subreddit(subreddit_name)
post_limit = 1000  # You can increase this

print(f"Downloading images from r/{subreddit_name}...")

for post in subreddit.new(limit=post_limit):
    url = post.url
    if url.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            img_data = requests.get(url).content
            filename = os.path.join(download_folder, os.path.basename(urlparse(url).path))
            with open(filename, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {url} - {e}")

print("Done.")
