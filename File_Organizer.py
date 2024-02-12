import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedStyle

def create_directory(directory):
    if not os.path.exists(directory):
        response = messagebox.askyesno("Directory Not Found", f"The directory '{directory}' does not exist. Do you want to create it?")
        if response:
            os.makedirs(directory)
            messagebox.showinfo("Directory Created", f"Directory '{directory}' created successfully.")
        else:
            messagebox.showwarning("Directory Not Created", f"Skipping creation of directory '{directory}'.")

def get_source_directory():
    source_directory = filedialog.askdirectory(title="Select Source Directory")
    return source_directory

def get_target_directory():
    target_directory = filedialog.askdirectory(title="Select Target Directory")
    return target_directory

def organize_files(source_dir, target_dir):
    if not source_dir or not target_dir:
        messagebox.showerror("Error", "Please select both source and target directories.")
        return

    # Define file extensions and corresponding directories
    extensions = {
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".bmp": "Images",
        ".txt": "Documents", ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
        ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents", ".pptx": "Documents",
        ".mp4": "Videos", ".avi": "Videos", ".mkv": "Videos", ".mov": "Videos", ".flv": "Videos",
        ".mp3": "Music", ".wav": "Music", ".ogg": "Music", ".flac": "Music",
        ".zip": "Archives", ".rar": "Archives", ".tar": "Archives", ".gz": "Archives",
        ".exe": "Executables", ".msi": "Executables", ".bat": "Executables", ".sh": "Executables",
        ".py": "Programming", ".java": "Programming", ".cpp": "Programming", ".c": "Programming",
        ".html": "Programming", ".css": "Programming", ".js": "Programming", ".php": "Programming"
    }

    # Create directories if they don't exist
    for directory in set(extensions.values()):
        create_directory(os.path.join(target_dir, directory))

    # Iterate through files in source directory and move them to appropriate directories
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file)):
            file_extension = os.path.splitext(file)[1].lower()
            destination_dir = extensions.get(file_extension, "Others")
            create_directory(os.path.join(target_dir, destination_dir))
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, destination_dir, file))

    messagebox.showinfo("Success", "Files organized successfully!")

def main():
    root = tk.Tk()
    root.title("File Organizer")
    style = ThemedStyle(root)
    style.set_theme("arc")

    def select_source_directory():
        source_directory.set(get_source_directory())

    def select_target_directory():
        target_directory.set(get_target_directory())

    def organize():
        organize_files(source_directory.get(), target_directory.get())

    source_directory = tk.StringVar()
    target_directory = tk.StringVar()

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Source Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(frame, textvariable=source_directory, state='readonly', width=40).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame, text="Browse", command=select_source_directory).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(frame, text="Target Directory:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(frame, textvariable=target_directory, state='readonly', width=40).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(frame, text="Browse", command=select_target_directory).grid(row=1, column=2, padx=5, pady=5)

    tk.Button(frame, text="Organize Files", command=organize).grid(row=2, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
