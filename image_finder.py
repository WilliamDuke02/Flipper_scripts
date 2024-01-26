import os
import shutil
import time

def unique_file(destination, filename):
    """Generate a unique filename to avoid overwriting existing files."""
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1

    return new_filename

def find_and_copy_images(destination_folder):
    # Drive root (e.g., C:\ on Windows)
    source_folder = os.path.abspath(os.sep)

    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the directories
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_file = os.path.join(root, file)
                # Generate a unique filename
                unique_name = unique_file(destination_folder, file)
                destination_file = os.path.join(destination_folder, unique_name)
                # Copy file
                shutil.copy2(source_file, destination_file)

# Example usage
destination = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Found Photos')
find_and_copy_images(destination)
