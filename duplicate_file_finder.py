import os
import hashlib
import csv
from collections import defaultdict

def get_file_hash(file_path, chunk_size=8192):
    """Generate SHA-256 hash for a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (OSError, PermissionError) as e:
        print(f"Error reading {file_path}: {e}")
        return None

def find_duplicate_files(folder_path):
    """Find duplicate files in a given folder and its subfolders based on hash values."""
    file_hashes = defaultdict(list)
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash:
                file_hashes[file_hash].append(file_path)
            else:
                print(f"Skipping file {file_path} due to hash error.")
    
    return {hash_val: paths for hash_val, paths in file_hashes.items() if len(paths) > 1}

def save_duplicates_to_csv(duplicates, output_file):
    """Save duplicate file information to a CSV file."""
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Original File", "Duplicate Copies", "Number of Duplicates", "Duplicate File Paths"])
        
        for paths in duplicates.values():
            original_file = paths[0]
            duplicate_files = paths[1:]
            for dup_file in duplicate_files:
                writer.writerow([original_file, os.path.basename(dup_file), len(duplicate_files), dup_file])

def main(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return
    
    output_csv = os.path.join(folder_path, "duplicate_files.csv")
    print("Scanning folder and subfolders...")
    
    duplicates = find_duplicate_files(folder_path)
    
    if duplicates:
        save_duplicates_to_csv(duplicates, output_csv)
        print(f"Duplicate file list saved to {output_csv}")
    else:
        print("No duplicate files found.")
