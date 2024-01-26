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

def should_exclude(path, exclusions):
    """Determine if a path should be excluded based on exclusion patterns."""
    for exclusion in exclusions:
        if exclusion in path:
            return True
    return False

def find_and_copy_images(destination_folder, exclusions):
    source_folder = os.path.abspath(os.sep)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        if should_exclude(root, exclusions):
            continue

        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_file = os.path.join(root, file)
                unique_name = unique_file(destination_folder, file)
                destination_file = os.path.join(destination_folder, unique_name)
                shutil.copy2(source_file, destination_file)

# Example usage
destination = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Found Photos')

# Add common patterns found in the directories you want to exclude
exclusions = [
    "Program Files", "AppData", "LocalLow", "Temp", "Packages",
    "ProgramData", "Windows", "NVIDIA Corporation", "VS Code", "Microsoft",
    "Flipper", ".minecraft", "DayZ Launcher", ".vscode", "GitHubDesktop",
    # Add any other common patterns here
]

find_and_copy_images(destination, exclusions)
