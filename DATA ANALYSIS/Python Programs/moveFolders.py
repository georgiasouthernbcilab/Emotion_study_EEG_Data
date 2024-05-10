import os
import shutil

def move_folders_with_avi_files(base_path):
    """
    Moves folders containing .avi files into a new parent folder called "Emotion Classification".

    :param base_path: The directory path to check for subfolders with .avi files.
    """
    # Path to the parent folder where subfolders will be moved
    target_path = os.path.join(base_path, "Emotion Classification")
    os.makedirs(target_path, exist_ok=True)

    # Iterate over each item in the base directory
    for item in os.listdir(base_path):
        folder_path = os.path.join(base_path, item)
        
        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Check each file in the directory for .avi extension
            contains_avi = any(file.endswith('.avi') for file in os.listdir(folder_path))
            
            # If an .avi file is found, move the folder
            if contains_avi:
                # New location for the subfolder
                new_folder_path = os.path.join(target_path, item)
                shutil.move(folder_path, new_folder_path)
                print(f"Moved {folder_path} to {new_folder_path}")

def main():
    current_path = os.path.dirname(os.path.realpath(__file__))
    move_folders_with_avi_files(current_path)

if __name__ == "__main__":
    main()
