import os
from tkinter import *
from tkinter import messagebox
from Drive import *
from convert_to_zip import *
from typing import Final
options = Tk()
options.title("Home Page")
# options frame
menu_frame = LabelFrame(options, text="Chose The Following", padx=100, pady=100)
menu_frame.pack(padx=50, pady=50)

login_status = False

def loggin():
    # loggin window
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
            ask_first_time_login = messagebox.askquestion('ask first time', 'Did you provide destination Folder ID?')
            if ask_first_time_login == 'no':
                messagebox.showinfo('change the id request', 'plz provide a destination id')
                Label(uploading, text="Enter your Drive File ID ").pack()
                folder_id = Entry(uploading, width=40)
                folder_id.pack(pady=5)
                def first_id():
                    main1(str(take_path), folder_id.get(), 'upload', "")
                    uploading.destroy()
                Button(uploading, text="Click to Continue",command=first_id).pack()
            else:
                ask_destination = messagebox.askquestion('taking destination', 'change the destination Id?')
                if ask_destination == 'yes':
                    Label(uploading, text="Enter your Drive File ID ").pack()
                    folder_id = Entry(uploading, width=40)
                    folder_id.pack(pady=5)
                    def change_id():
                        main1(str(take_path), str(folder_id.get()), 'upload',"")
                        uploading.destroy()
                    Button(uploading, text="Click to Continue", command= change_id).pack()
                    #uploading.destroy()
                else:
                    #Label(uploading, text=str(fixed_id)+'hii').pack()
                    main1(str(take_path), "", 'upload', "")
                    uploading.destroy()

        def zipping(take_path):
            zipp =Toplevel()
            zipp.title("zip a file")
            zipp.geometry('400x250')
            Label(zipp, text="Enter ZIP File Name").pack()
            file_name = Entry(zipp, width=50)
            file_name.pack(pady=5)

            def zip_fun(path_passing):
                main(str(path_passing), str(file_name.get()))
                give_path = os.getcwd()
                path = f"{file_name.get()}" + ".zip"
                uploading = Toplevel()
                uploading.title('Taking Path & ID')
                uploading.geometry('400x100')
                ask_first_time_login = messagebox.askquestion('ask first time', 'Did you provide destination Folder ID?')
                if ask_first_time_login == 'no':
                    messagebox.showinfo('change the id request', 'plz provide a destination id')
                    Label(uploading, text="Enter your Drive File ID ").pack()
                    folder_id = Entry(uploading, width=40)
                    folder_id.pack(pady=5)
                    def first_id():
                        main1(str(give_path), folder_id.get(), '', path)
                        uploading.destroy()
                        zipp.destroy()
                    Button(uploading, text="Click to Continue", command=first_id).pack()
                else :
                    main1(str(give_path), "", '', path)
                    uploading.destroy()
                    zipp.destroy()
            Button(zipp, text="Enter", command= lambda :zip_fun(take_path)).pack()

        def list_files(take_path):
            main1(take_path, "", "list_files","")

        backup_frame = LabelFrame(backups, text="Create a Backup", padx=100, pady=100)
        backup_frame.pack(padx=50, pady=50)
        Button(backup_frame, text="Upload to Google Drive", command=lambda : upload(path)).pack()
        Button(backup_frame, text="convert Backup File to ZIP & upload to Drive",command= lambda :zipping(path)).pack()
        Button(backup_frame, text="Download from Drive").pack()
        Button(backup_frame, text="files in Google Drive backup", command=lambda :list_files(path)).pack()
        Button(backup_frame, text="back to Home Page", command=backups.destroy).pack()


    Label(takingdirc_path,text="Enter the Backup folder Path").pack()
    backup_path = Entry(takingdirc_path, width=50)
    backup_path.pack()
    Button(takingdirc_path,text="Enter",command=lambda :taking_path(backup_path.get())).pack()

def logout():
    messagebox.showinfo('Logging Out','Thank You for using File Manager')
    options.destroy()


blog = Button(menu_frame, text="Login", command=loggin).grid(row=0, column=0)
b1 = Button(menu_frame, text="Work on File", command= window31).grid(row=1, column=0)
b2 = Button(menu_frame, text="Make A Backup", command= window32).grid(row=2, column=0)
b3 = Button(menu_frame, text="Log Out", command=logout).grid(row=3, column=0)
options.mainloop()