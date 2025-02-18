import tkinter as tk
from tkinter import filedialog, messagebox
import os
import duplicate_file_finder  # Importing the logic script

def select_folder():
    """Opens a file dialog to select a folder."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def scan_duplicates():
    """Calls the logic script to scan for duplicate files."""
    folder = folder_path.get()
    if not os.path.isdir(folder):
        messagebox.showerror("Error", "Please select a valid folder")
        return
    
    duplicate_file_finder.main(folder)  # Call the main function from the logic file
    messagebox.showinfo("Success", f"Duplicate file report generated in {folder}")

# Create UI window
root = tk.Tk()
root.title("Duplicate File Finder")
root.geometry("500x250")

folder_path = tk.StringVar()

# UI Elements
label = tk.Label(root, text="Select Folder to Scan:")
label.pack(pady=5)

entry = tk.Entry(root, textvariable=folder_path, width=60)
entry.pack(pady=5)

browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.pack(pady=5)

scan_button = tk.Button(root, text="Scan for Duplicates", command=scan_duplicates)
scan_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

# Run UI
root.mainloop()
