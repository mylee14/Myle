import tkinter as tk
from tkinter import ttk, messagebox
import configparser
import subprocess

class PresetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Preset Selector GUI")

        # Load settings
        self.config = configparser.ConfigParser()
        self.config.read('../settings.ini')
        self.presets = int(self.config['Settings']['presets'])
        self.geometry = self.config['Settings']['geometry']

        # application window
        self.root.geometry(self.geometry)

        # Create and place the dropdown menu
        self.preset_label = tk.Label(root, text="Select Preset:")
        self.preset_label.pack(pady=10)

        self.preset_var = tk.StringVar()
        preset_values = [self.config['Presets'][str(i+1)] for i in range(self.presets) if self.config['Presets'][str(i+1)]]
        self.preset_dropdown = ttk.Combobox(root, textvariable=self.preset_var)
        self.preset_dropdown['values'] = preset_values
        self.preset_dropdown.current(0)
        self.preset_dropdown.pack(pady=10)

        # Create and place
        self.generate_button = tk.Button(root, text="Generate", command=self.generate)
        self.generate_button.pack(pady=10)

    def generate(self):
        selected_preset = self.preset_var.get()
        # Call generator.py with the selected presets
        subprocess.run(['python3', 'generate.py', selected_preset])
        messagebox.showinfo("Generate", "Generated Content!")
        self.root.destroy()  # Close the application

if __name__ == "__main__":
    root = tk.Tk()
    app = PresetApp(root)
    root.mainloop()