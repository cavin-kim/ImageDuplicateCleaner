import os
import hashlib

def remove_duplicates(directory):
    hash_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash not in hash_dict:
                hash_dict[file_hash] = file_path
            else:
                # Remove duplicate file
                os.remove(file_path)

# Replace 'directory_path' with the path to your dataset directory
remove_duplicates('directory_path')
