import os
from tkinter import messagebox


def deleting(file_path,file_name):
    try:
        for file in os.listdir(file_path):
            files = file.split('.')
            if (len(files)==1):
                for in_files in os.listdir(f'{file_path}/{files[0]}'):
                    if(in_files == file_name):
                        os.remove(f'{file_path}/{files[0]}/{file_name}')
                        messagebox.showinfo('Confrimation','File is removed')
            if (file == file_name):
                os.remove(f'{file_path}/{file_name}')
                messagebox.showinfo('Confrimation', 'File is removed')
    except FileNotFoundError:
        messagebox.showinfo('confirmation','File not found')
