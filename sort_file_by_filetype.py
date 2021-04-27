import os
import os as os1
import tkinter as tk
from cffi.backend_ctypes import xrange
from pathlib import Path

def sort_type1(request,file_path):
    global sorted
    if(request=="file size"):
        """ Return list of file paths in directory sorted by file size """
        root = tk.Tk()
        root.title('Sort by Size')
        # Get list of files
        filepaths = []
        for basename in os1.listdir(file_path):
            filename = os1.path.join(file_path, basename)
            if os1.path.isfile(filename):
                filepaths.append(filename)

        # Re-populate list with filename, size tuples
        for i in xrange(len(filepaths)):
            filepaths[i] = (filepaths[i], os1.path.getsize(filepaths[i]))

        filepaths.sort(key=lambda filename: filename[1], reverse=True)

        # Re-populate list with just filenames
        for i in xrange(len(filepaths)):
            filepaths[i] = filepaths[i][0]
        file = ""
        for i in filepaths:
            file = file + '\n' + i
        tk.Label(root,text= file).pack()
        tk.Button(root,text='Ok',command=root.destroy).pack()
        root.mainloop()

    elif(request == "last modified") :
        root = tk.Tk()
        root.title('Sort by Size')
        paths = sorted(Path(file_path).iterdir(), key=os.path.getmtime)
        file = ""
        for i in paths:
            file = file + '\n' + str(i)
        tk.Label(root, text=file).pack()
        tk.Button(root, text='Ok', command=root.destroy).pack()
        root.mainloop()

    elif(request=="Name"):
        root = tk.Tk()
        root.title('Sort by Size')
        sorted = sorted(os1.listdir(file_path))
        files = ""
        for file in sorted:
            files = files + "\n" + file
        tk.Label(root, text=files).pack()
        tk.Button(root, text='Ok', command=root.destroy).pack()
        root.mainloop()



