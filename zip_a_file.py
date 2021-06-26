import shutil
import os
from tkinter import messagebox as mb, filedialog


def zip(filename,request,file_path):
    if(request=='compress_dirc'):
        filename1= file_path
    else :
        mb.showinfo('Select ZIP', 'select the file to ZIP')
        filename1 = filedialog.askdirectory(initialdir="C:\desktop", title="select a zip file")
    mb.showinfo('Save as','Enter the destination of ZIP file')
    extract_dir = filedialog.askdirectory(initialdir="C:\desktop", title="Save as")
    archive_format = "zip"
    shutil.make_archive(f'{extract_dir}/{filename}', archive_format,root_dir=filename1)
    mb.showinfo('ZIP status','file is zipped succesfully')
    os.startfile(f'{extract_dir}/{filename}.zip')
    zip_path_for_secure_folder = f'{extract_dir}/{filename}.zip'
    return zip_path_for_secure_folder

