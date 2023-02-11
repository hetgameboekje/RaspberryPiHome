import os
import hashlib

def hash_file(filename):
    """Calculate the hash of a file."""
    h = hashlib.sha1()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()

def find_duplicate_files(folder):
    """Find and move duplicate files in a folder to a subfolder."""
    # Dictionary to store hashes of files
    hashes = {}

    # Iterate over the files in the folder
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            # Add the hash to the dictionary
            if file_hash in hashes:
                # If the hash is already in the dictionary, this is a duplicate file
                hashes[file_hash].append(file_path)
            else:
                hashes[file_hash] = [file_path]
    # User input > duplicates_folder = input("file location")
    duplicates_folder = './duplicated_files'

    # Create the duplicates folder if it doesn't already exist
    if not os.path.exists(duplicates_folder):
        os.makedirs(duplicates_folder)

    # Iterate over the dictionary of hashes
    for key, value in hashes.items():
        if len(value) > 1:
            # This is a list of duplicate files
            for file in value[1:]:
                # Move the duplicate file to the duplicates folder
                os.rename(file, os.path.join(duplicates_folder, os.path.basename(file)))

# Find and move duplicate files in the specified folder
find_duplicate_files('./')

# User input > find_duplicate_files = input("file location")

#update 