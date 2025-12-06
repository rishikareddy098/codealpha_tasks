import os
import shutil
import re
import requests


source_folder = "C:/Users/T MOBILE/Downloads"
destination_folder = "C:/Users/T MOBILE/OneDrive/Pictures/JPG_Files"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

def download_sample_image():
    url = "https://picsum.photos/200"   
    response = requests.get(url)

    if response.status_code == 200:
        with open(os.path.join(source_folder, "sample.jpg"), "wb") as file:
            file.write(response.content)
        print("Sample image downloaded.")
    else:
        print("Failed to download image.")

download_sample_image()

def move_jpg_files():
    jpg_pattern = re.compile(r".*\.jpg$", re.IGNORECASE)

    print("\nScanning folder:", source_folder)

    for filename in os.listdir(source_folder):
        if jpg_pattern.match(filename):       
            src = os.path.join(source_folder, filename)
            dest = os.path.join(destination_folder, filename)
            
            shutil.move(src, dest)
            print(f"Moved: {filename}")
    
    print("\nAll JPG files moved successfully!")

move_jpg_files()