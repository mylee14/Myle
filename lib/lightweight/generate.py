import os
import requests
import configparser

def create_directories(base_path, num_presets):
    os.makedirs(base_path, exist_ok=True)
    for i in range(1, num_presets + 1):
        os.makedirs(os.path.join(base_path, str(i)), exist_ok=True)

def fetch_images(api_url, api_key, num_presets):
    response = requests.get(api_url, params={'api_key': api_key, 'presets': num_presets})
    response.raise_for_status()
    return response.json()

def save_images(base_path, images):
    for preset, image_list in images.items():
        preset_number = preset.split('_')[1]  # Extract the preset number from the key
        preset_dir = os.path.join(base_path, preset_number)
        for img_url in image_list:
            img_data = requests.get(img_url).content
            img_name = os.path.basename(img_url)
            with open(os.path.join(preset_dir, img_name), 'wb') as img_file:
                img_file.write(img_data)

def create_text_files(base_path, num_presets):
    for i in range(1, num_presets + 1):
        preset_dir = os.path.join(base_path, str(i))
        with open(os.path.join(preset_dir, 'confirm.txt'), 'w') as f:
            f.write('Confirm result:\n')
        with open(os.path.join(preset_dir, 'validate.txt'), 'w') as f:
            f.write('Validate result:\n')

def main():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    
    api_url = config['API']['URL']
    api_key = config['API']['KEY']
    num_presets = int(input("Enter number of presets (default is 4): ") or "4")
    base_path = os.path.join('repo_data')

    create_directories(base_path, num_presets)
    images = fetch_images(api_url, api_key, num_presets)
    save_images(base_path, images)
    create_text_files(base_path, num_presets)

if __name__ == "__main__":
    main()