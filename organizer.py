import os
import shutil

folder = input("Enter the folder to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"]
}

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    if not os.path.isfile(filepath):
        continue

    name, extension = os.path.splitext(filename)
    extension = extension.lower()

    for category, extensions in file_types.items():
        if extension in extensions:
            destination = os.path.join(folder, category)
            os.makedirs(destination, exist_ok=True)
            shutil.move(filepath, os.path.join(destination, filename))
            print(f"Moved {filename} to {category}")
            break