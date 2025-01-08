import sys

def generate_data(preset):
    # Perform the specific job based on the selected preset
    print(f"Generating data for {preset}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generator.py <preset>")
        sys.exit(1)
    
    preset = sys.argv[1]
    generate_data(preset)