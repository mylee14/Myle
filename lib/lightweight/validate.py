import os
import shutil
import zipfile
import configparser
from datetime import datetime

def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                           os.path.join(directory_path, '..')))

def main():
    base_path = 'repo_data'
    current_date = datetime.now().strftime('%Y-%m-%d')
    zip_path = f"{base_path}-{current_date}.zip"
    
    zip_directory(base_path, zip_path)
    print(f"Zipped directory created at: {zip_path}")

    # Remove the repo_data directory after zipping
    shutil.rmtree(base_path)
    print(f"Directory {base_path} has been removed.")

if __name__ == "__main__":
    main()