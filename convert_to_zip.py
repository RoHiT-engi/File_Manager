import shutil
from os import path
from tkinter import messagebox
from tkinter import *
def main(file_path,zip_file_name):
    if path.exists(file_path):
        src = path.relpath(file_path);
    else:
        messagebox.showerror("Invalid path","Invalid path")
    shutil.make_archive(zip_file_name,"zip",src)

    messagebox.showinfo('File created','your file is created in app diectory succesfully')
    #Label(created,text="ZIP File is created succesfully in app directiory").pack()

if __name__=="__main__":
    main()