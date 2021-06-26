import shutil
import os
from tkinter import messagebox as mb, filedialog


def unzip(check):
    mb.showinfo('Select ZIP','select the ZIP file')
    filename1 = filedialog.askopenfilename(initialdir="C:", title="select a zip file",filetypes=[("zipfiles","*.zip")])
    mb.showinfo('Save as','Enter the destination of ZIP extraction')
    extract_dir = filedialog.askdirectory(initialdir="C:", title="Save as")
    archive_format = "zip"
    shutil.unpack_archive(filename1, extract_dir, archive_format)
    mb.showinfo('UnZIP status','file is unzipped successfully')
    if (check==True):
        os.remove(filename1)


