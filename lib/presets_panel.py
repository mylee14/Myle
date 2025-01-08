import tkinter as tk
from tkinter import ttk, messagebox
import configparser
import subprocess

class PresetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Preset Selector GUI")

        # Load settings from settings.ini
        self.config = configparser.ConfigParser()
        self.config.read('../settings.ini')
        self.presets = int(self.config['Settings']['presets'])

        # Create and place the dropdown menu
        self.preset_label = tk.Label(root, text="Select Preset:")
        self.preset_label.pack(pady=10)

        self.preset_var = tk.StringVar()
        preset_values = [self.config['Presets'][str(i+1)] for i in range(self.presets) if self.config['Presets'][str(i+1)]]
        self.preset_dropdown = ttk.Combobox(root, textvariable=self.preset_var)
        self.preset_dropdown['values'] = preset_values
        self.preset_dropdown.current(0)
        self.preset_dropdown.pack(pady=10)

        # Create and place the "Generate" button
        self.generate_button = tk.Button(root, text="Generate", command=self.generate)
        self.generate_button.pack(pady=10)

        # Create and place the "Confirm" button
        self.confirm_button = tk.Button(root, text="Confirm", command=self.confirm)
        self.confirm_button.pack(pady=10)
        self.confirm_button.config(state=tk.DISABLED)  # Initially disabled

    def generate(self):
        selected_preset = self.preset_var.get()
        # Call generator.py with the selected preset
        subprocess.run(['python3', 'generator.py', selected_preset])
        messagebox.showinfo("Generate", f"Generated folders for {selected_preset}")
        # Enable the "Confirm" button after generation
        self.confirm_button.config(state=tk.NORMAL)

    def confirm(self):
        # Perform the confirm action
        messagebox.showinfo("Confirm", "Confirmed the generated folders")
        self.confirm_button.config(state=tk.DISABLED)  # Disable the button after confirming

if __name__ == "__main__":
    root = tk.Tk()
    app = PresetApp(root)
    root.mainloop()