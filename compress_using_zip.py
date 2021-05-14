import shutil
from os import path
from tkinter import messagebox, filedialog
import os


def main(file_path, zip_file_name):
    global src
    if path.exists(file_path):
        src = path.relpath(file_path);
    else:
        messagebox.showerror("Invalid path", "Invalid path")
    dest = filedialog.askdirectory(initialdir="C:", title="select a directory to save")
    print(dest)
    shutil.make_archive(f'{dest}/{zip_file_name}',"zip",root_dir=src)
    messagebox.showinfo('File created status', 'your file is created in given diectory succesfully')
    os.startfile(f'{dest}/{zip_file_name}.zip')
    zip_path_for_secure_folder= f'{dest}/{zip_file_name}.zip'
    return zip_path_for_secure_folder
