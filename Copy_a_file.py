import os
import shutil
from tkinter import filedialog
from tkinter import messagebox as mb

def copying(file_path,file_name):
    source = file_path + '/' + file_name
    destination1 = filedialog.askdirectory()
    shutil.copy(source, destination1)
    mb.showinfo('confirmation', "File Copied !")

