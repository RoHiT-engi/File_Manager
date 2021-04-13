import os
from tkinter import messagebox as mb
def renameing(file_path,file_name,new_file_name):
    chosenFile = f'{file_path}/{file_name}'
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    newName = new_file_name
    path = os.path.join(path1, newName + extension)
    os.rename(chosenFile, path)
    mb.showinfo('confirmation', "File Renamed !")

