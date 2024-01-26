import os
import shutil

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
    user_folder = os.path.expanduser("~")  # Get the user's home directory
    appdata_folder = os.path.join(user_folder, 'AppData')  # Get the AppData folder path

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(user_folder):
        # Check if the current directory is the AppData folder or any of its subdirectories
        if appdata_folder in root:
            continue

        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_file = os.path.join(root, file)
                unique_name = unique_file(destination_folder, file)
                destination_file = os.path.join(destination_folder, unique_name)
                shutil.copy2(source_file, destination_file)

if __name__ == "__main__":
    destination_folder = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Found Photos')

    find_and_copy_images(destination_folder)
