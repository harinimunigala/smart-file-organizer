import os
import shutil
import re

folder_path =input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".txt", ".docx", ".pptx"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    
    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    
    return "Others"

def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def clean_filename(filename):
    name, ext = os.path.splitext(filename)
    
    name = name.lower()
    name = re.sub(r'[^a-z0-9]', '_', name)
    name = re.sub(r'_+', '_', name)
    
    return name + ext

def get_unique_name(path):
    base, ext = os.path.splitext(path)
    counter = 1
    
    while os.path.exists(path):
        path = f"{base}_{counter}{ext}"
        counter += 1
    
    return path

files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        category = get_category(file)
        category_path = os.path.join(folder_path, category)
        
        print(f"Moving {file} → {category}")
        
        create_folder_if_not_exists(category_path)
        
        clean_name = clean_filename(file)
        destination = os.path.join(category_path, clean_name)
        destination = get_unique_name(destination)
        
        shutil.move(file_path, destination)

print("Files organized successfully!")
