from bs4 import BeautifulSoup
import requests
import os

# PASTE THE URL WITHIN THE QUOTES
BUNKR_URL = "Bunkr.is URL"

# PASTE THE PATH WITHIN THE QUOTES
FOLDER_PATH = "FOLDER PATH"   # eg: "C:/Users/User/Desktop/New folder"


headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=BUNKR_URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")


pictures = soup.find_all(name='a', class_='image')
print(f"{len(pictures)} images found")

picture_links = [link.get("href") for link in pictures]
# print(picture_links)


os.chdir(FOLDER_PATH)
print(os.getcwd())

counter = 0
for image in picture_links:
    r = requests.get(image)

    print(f"Downloading image {counter}...")
    with open(f"image{counter}.jpg", 'wb') as f:
        f.write(r.content)
    counter += 1

print("Download Completed")
