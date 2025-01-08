import sys
import os
import configparser
import instaloader

def generate_folders(preset):
    base_dir = 'value_presets'
    
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Create the number of folders specified by the preset
    num_folders = int(preset)
    for i in range(1, num_folders + 1):
        folder_path = os.path.join(base_dir, str(i))
        os.makedirs(folder_path, exist_ok=True)
    
    print(f"Generated {num_folders} folders in '{base_dir}'")
    return num_folders

def download_instagram_posts(tag, posts_per_folder, num_folders):
    L = instaloader.Instaloader()

    for i in range(1, num_folders + 1):
        folder_path = os.path.join('value_presets', str(i))
        # Download posts for the given tag
        posts = instaloader.Hashtag.from_name(L.context, tag).get_posts()
        count = 0
        for post in posts:
            if count >= posts_per_folder:
                break
            L.download_post(post, target=folder_path)
            count += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generator.py <preset>")
        sys.exit(1)
    
    preset = sys.argv[1]

    # Load settings from settings.ini
    config = configparser.ConfigParser()
    config.read('settings.ini')
    tag = config['Settings']['data_tag']
    value_per_preset = int(config['Settings']['value_per_preset'])

    num_folders = generate_folders(preset)
    download_instagram_posts(tag, value_per_preset, num_folders)