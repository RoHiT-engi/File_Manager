from tkinter import *
from tkinter import messagebox
from subprocess import call

from convert_to_zip import *
options = Tk()
options.title("Home Page")
#uploading_to_drive = call(["uploading_to_drive","C:/Users/91922/PycharmProjects/file_manager/uploading _to_Drive.py"])
# options frame
menu_frame = LabelFrame(options, text="Chose The Following", padx=100, pady=100)
menu_frame.pack(padx=50, pady=50)

login_status = False


def loggin():
    #loggin window
    login = Toplevel()
    login.title('File Manager & Recovery System')
    login.geometry('500x500')
    # login window1
    login_frame = LabelFrame(login, text="login", padx=10, pady=100)
    login_frame.pack(padx=50, pady=50)

    login_label = Label(login_frame, text="Login ID")
    login_label.grid(row=0, column=0)
    login_text_field = Entry(login_frame, width=40)
    login_text_field.grid(row=0, column=1)

    pass_label = Label(login_frame, text="Password")
    pass_label.grid(row=1, column=0)
    pass_text_field = Entry(login_frame, width=40)
    pass_text_field.grid(row=1, column=1, pady=5)

    def logging():
        #making login_status
        if (login_text_field.get() == "") and (pass_text_field.get() == ""):
            global login_status
            login_status = True
            login.destroy()
    enter = Button(login_frame, text="Enter", command=logging).grid(row=3, column=1)


def window31():
    # work on file
    def working(take_path):
        def zip_fun1(path_passing):
            zipp1 = Toplevel()
            zipp1.title('Make a ZIP file')
            zipp1.geometry('400x100')
            workfile.destroy()
            Label(zipp1, text="Enter ZIP File Name").pack()
            file_name = Entry(zipp1, width=50)
            file_name.pack(pady=5)
            Button(zipp1, text="Enter", command=lambda: main(str(path_passing), str(file_name.get()))).pack()
        # workonfile.destroy()
        workfile = Toplevel()
        workfile.title('Chose the Work')
        workfile.geometry('500x500')
        workonfile.destroy()

        work_on_file = LabelFrame(workfile, text="Chose The Work To Do", padx=100, pady=100)
        work_on_file.pack(padx=50, pady=50)

        Button(work_on_file, text="Seperate File").grid(row=0, column=0)
        Button(work_on_file, text="Convert to ZIP File",command=lambda :zip_fun1(take_path)).grid(row=1, column=0)
        Button(work_on_file, text="open a file for YOU").grid(row=2, column=0)
        Button(work_on_file, text="Search a file").grid(row=0, column=1)
        Button(work_on_file, text="Sort a File").grid(row=1, column=1)
        Button(work_on_file, text="Make a secure Folder").grid(row=2, column=1)
        Button(work_on_file, text="delete a file").grid(row=3,column=0)

    #making Toplevel
    workonfile = Toplevel()
    workonfile.title('Working On File')
    workonfile.geometry('400x150')
    if login_status == False:
        messagebox.showwarning('Invalid Access', 'Login to Proceed')
        workonfile.destroy()
    Label(workonfile, text="Enter the Directory Path ").pack()
    file_path_dirc = Entry(workonfile, width=40)
    file_path_dirc.pack(pady=5)
    Button(workonfile, text="Enter", command=lambda :working(str(file_path_dirc.get()))).pack()


def window32():
    # create Backup
    # making top level
    takingdirc_path = Toplevel()
    takingdirc_path.title("Taking Path")
    takingdirc_path.geometry('400x100')
    if login_status == False:
        messagebox.showwarning('Invalid Access', 'Login to Proceed')
        takingdirc_path.destroy()
    def taking_path(path):
        backups = Toplevel()
        backups.title('Create the Backup')
        backups.geometry('500x500')
        takingdirc_path.destroy()
        global backup_frame
        def upload(take_path):
            uploading = Toplevel()
            uploading.title('Taking Path & ID')
            uploading.geometry('400x100')
            backups.destroy()
            #folder_id = ""
            taking_ID = Label(uploading, text="Enter your Drive File ID ").pack()
            folder_id = Entry(uploading, width=40)
            folder_id.pack(pady=5)

            Button(uploading, text="Enter").pack()
        def zipping(take_path):
            zipp =Toplevel()
            zipp.title("zip a file")
            zipp.geometry('400x250')
            backups.destroy()
            Label(zipp, text="Enter ZIP File Name").pack()
            file_name = Entry(zipp, width=50)
            file_name.pack(pady=5)

            def zip_fun(path_passing):
                main(str(path_passing), str(file_name.get()))
                zipp.destroy()
            Button(zipp, text="Enter", command= lambda :zip_fun(take_path)).pack()

        backup_frame = LabelFrame(backups, text="Create a Backup", padx=100, pady=100)
        backup_frame.pack(padx=50, pady=50)
        Button(backup_frame, text="Upload to Google Drive", command=lambda : upload(path)).pack()
        Button(backup_frame, text="convert Backup File to ZIP",command= lambda :zipping(path)).pack()
        Button(backup_frame, text="Download from Drive").pack()
        Button(backup_frame, text="files in Google Drive backup").pack()
    Label(takingdirc_path,text="Enter the Backup folder Path").pack()
    backup_path = Entry(takingdirc_path, width=50)
    backup_path.pack()
    Button(takingdirc_path,text="Enter",command=lambda :taking_path(backup_path.get())).pack()


blog = Button(menu_frame, text="Login", command=loggin).grid(row=0, column=0)
b1 = Button(menu_frame, text="Work on File", command= window31).grid(row=1, column=0)
b2 = Button(menu_frame, text="Make A Backup", command= window32).grid(row=2, column=0)
b3 = Button(menu_frame, text="Exit", command=options.destroy).grid(row=3, column=0)
options.mainloop()