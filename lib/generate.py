import sys
import os

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generator.py <preset>")
        sys.exit(1)
    
    preset = sys.argv[1]
    generate_folders(preset)