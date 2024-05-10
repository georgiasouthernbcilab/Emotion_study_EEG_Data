import os
import shutil

def move_folders_with_avi_files(base_path):
    """
    Moves folders with not enough files into an "Incomplete Experiment" folder.

    """
    # Path to the parent folder where subfolders will be moved
    target_path = os.path.join(base_path, "Incomplete Experiment")
    os.makedirs(target_path, exist_ok=True)

    # Iterate over each item in the base directory
    for item in os.listdir(base_path):
        folder_path = os.path.join(base_path, item)
        
        # Check if the item is a directory
        if os.path.isdir(folder_path):
            item_count = 0
            # Check each file in the directory for .avi extension
            for item in os.listdir(folder_path):
                item_count +=1 
            if item_count <3:
                # New location for the subfolder
                new_folder_path = os.path.join(target_path, item)
                shutil.move(folder_path, new_folder_path)
                print(f"Moved {folder_path} to {new_folder_path}")

def main():
    current_path = os.path.dirname(os.path.realpath(__file__))
    move_folders_with_avi_files(current_path)

if __name__ == "__main__":
    main()
