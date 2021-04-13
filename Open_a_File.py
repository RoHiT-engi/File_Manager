import os
from tkinter import messagebox
def searching(file_path ,file_name):
    try:
        for file in os.listdir(file_path):
            files = file.split('.')
            if (len(files)==1):
                searching(f'{file_path}/{files[0]}',file_name)
                if(file == file_name):
                    os.startfile(f'{file_path}/{files[0]}/{file_name}')
            if (file == file_name):
                os.startfile(f'{file_path}/{file_name}')
    except FileNotFoundError:
        messagebox.showinfo('confirmation','File not found')

#searching('C:/Users/91922/Desktop/hllu','hello1.txt')