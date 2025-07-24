import os
import shutil

source_folder = "C:/Users/Vimal/Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"]
}

# Create destination folders
for folder in file_types:
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)


for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(filename)

    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            destination = os.path.join(source_folder, folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved {filename} to {folder}")
            break