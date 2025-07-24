# Python-Automation-Task
This is a simple Python automation script that organizes files in your Downloads folder into categorized folders based on their file types — such as **Images**, **Documents**, **Videos**, and **Music**.

## How It Works

The script:
- Scans your Downloads folder.
- Checks each file's extension (like `.jpg`, `.pdf`, `.mp3`, etc.).
- Moves files into appropriate subfolders:
  - Images
  - Documents
  - Videos
  - Music

All folders are automatically created if they don’t already exist.

## File Types Supported

| Category   | Extensions                          |
|------------|--------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`     |
| Documents  | `.pdf`, `.docx`, `.txt`, `.xlsx`    |
| Videos     | `.mp4`, `.mkv`, `.mov`, `.avi`      |
| Music      | `.mp3`, `.wav`, `.flac`             |

## How to Use

1. **Edit the source folder path** in the script:
   ```python
   source_folder = "C:/Users/Vimal/Downloads"
