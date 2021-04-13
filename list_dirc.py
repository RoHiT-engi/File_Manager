import os
import tkinter as tk
def listing(file_path):
    root = tk.Tk()
    root.title('Files in Directory')
    files = ""
    for file in os.listdir(file_path):
        files = files + '\n' +file
    lbl = tk.Label(root, text=files)
    lbl.pack()
    root.mainloop()
