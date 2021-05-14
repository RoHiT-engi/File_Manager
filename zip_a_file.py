import shutil
import os
from tkinter import messagebox as mb, filedialog


def zip(filename):
    mb.showinfo('Select ZIP','enter the file to ZIP')
    filename1 = filedialog.askdirectory(initialdir="C:", title="select a zip file")
    mb.showinfo('Save as','Enter the destination of ZIP file')
    extract_dir = filedialog.askdirectory(initialdir="C:", title="Save as")
    archive_format = "zip"
    shutil.make_archive(f'{extract_dir}/{filename}', archive_format,root_dir=filename1)
    mb.showinfo('ZIP status','file is zipped succesfully')
    os.startfile(f'{extract_dir}/{filename}.zip')

