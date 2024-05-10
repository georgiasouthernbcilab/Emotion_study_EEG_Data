import os
import shutil

def organize_files_by_prefix(path, num_chars):
    """
    Organizes files into folders based on the first num_chars characters of their filenames.

    :param path: The directory path to organize.
    :param num_chars: The number of characters to use for the folder naming.
    """
    if not os.path.isdir(path):
        raise ValueError("The provided path is not a directory")

    # Dictionary to keep track of prefixes and files
    prefix_dict = {}

    # Collect all files by their prefixes
    for filename in os.listdir(path):
        # Consider only files, ignore directories
        if os.path.isfile(os.path.join(path, filename)):
            prefix = filename[:num_chars]

            if prefix not in prefix_dict:
                prefix_dict[prefix] = []

            prefix_dict[prefix].append(filename)

    # Create directories and move files
    for prefix, files in prefix_dict.items():
        if len(files) > 1:  # Only process if more than one file shares the prefix
            new_dir = os.path.join(path, prefix)
            os.makedirs(new_dir, exist_ok=True)

            for file in files:
                shutil.move(os.path.join(path, file), os.path.join(new_dir, file))
                print(f"Moved {file} to {new_dir}/")

def main():
    current_path = os.path.dirname(os.path.realpath(__file__))
    num_chars = int(input("Enter the number of characters to use for file grouping: "))
    organize_files_by_prefix(current_path, num_chars)

if __name__ == "__main__":
    main()
