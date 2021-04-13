import os
import shutil
from tkinter import filedialog
from tkinter import messagebox as mb

def move_a_file(file_path,file_name):
    source = file_path + '/' + file_name
    destination =filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")