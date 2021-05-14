import os
import shutil
from tkinter import filedialog
from tkinter import messagebox as mb
def copying():
    source = filedialog.askdirectory()
    destination1 = filedialog.askdirectory()
    shutil.copy(source, destination1)
    mb.showinfo('confirmation', "File Copied !")
copying()