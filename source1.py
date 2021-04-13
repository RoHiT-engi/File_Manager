import os
from tkinter import *
from tkinter import messagebox
from Drive import *
from convert_to_zip import *
from typing import Final
from encrypting_file import *
from decrepting_file import *
from sort_using_extention import *
from New_file import *
from Open_a_File import *
from list_dirc import *
from Delete_a_file import *
from sort_file_by_filetype import *
from Copy_a_file import *
from Move_a_file import *
from Rename_a_file import *

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

    Checkbutton(login_frame, text="Remember ME").grid(row=2,columnspan=2)

    def logging():
        # making login_status
        if (login_text_field.get() == "") and (pass_text_field.get() == ""):
            global login_status
            login_status = True
            login.destroy()

    Button(login_frame, text="Enter", command=logging).grid(row=3, columnspan=2)


def window31():
    # work on file
    def working(take_path):
        def zip_fun1(path_passing):
            zipp1 = Toplevel()
            zipp1.title('Make a ZIP file')
            zipp1.geometry('400x100')
            Label(zipp1, text="Enter ZIP File Name").pack()
            file_name = Entry(zipp1, width=50)
            file_name.pack(pady=5)
            def zipping(take_path):
                main(str(take_path), str(file_name.get()))
                zipp1.destroy()
            Button(zipp1, text="Enter", command=lambda: zipping(path_passing)).pack()
        def secure_folder(path_passing):
            zipp1 = Toplevel()
            zipp1.title('Make a Secure file')
            zipp1.geometry('400x100')
            Label(zipp1, text="Enter Secure Folder Name").pack()
            file_name = Entry(zipp1, width=50)
            file_name.pack(pady=5)
            def things_to_do(file_name):
                encrypt = Toplevel()
                zipp1.destroy()
                encrypt.title('Making a secure folder')
                main(str(path_passing), str(file_name))
                Button(encrypt, text="encrypt the file", command=lambda: encrypting(file_name)).pack()
                Button(encrypt, text="decrypt the file", command=lambda: decrypting(file_name)).pack()
                Button(encrypt, text="open the encrypted file", command=lambda: os.startfile('your_encrypted_file.encrypted')).pack()


            Button(zipp1, text="Enter", command=lambda: things_to_do(file_name.get())).pack()
        def sort_by_ext(path_passing):
            window = Toplevel()
            window.title('Sort File By Extention')
            workfile.geometry('500x500')
            click = StringVar()
            click.set('Select the Extention')
            drop = OptionMenu(window, click, ".txt", ".mp3", ".mp4", ".pptx", ".jpg", ".jpeg", ".png", ".doc", ".docx", ".pdf")
            drop.pack()
            def sort(clicked_val):
                window.destroy()
                sort_using_extention(path_passing,clicked_val)

            Button(window, text="Enter", command=lambda: sort(click.get())).pack()
        def new(path_passing):
            window = Toplevel()
            window.title('Create New file')
            workfile.geometry('500x500')
            click = StringVar()
            click.set('Select the File')
            drop = OptionMenu(window, click, "text", "ppt", "Word", "Excel", "bitmap image", "New Folder", "ZIP")
            drop.pack()
            Label(window, text="Enter the file name").pack()
            new_file_name = Entry(window,width=50)
            new_file_name.pack()
            def New(clicked_val,file_name):
                window.destroy()
                new_file_creation(clicked_val, path_passing, file_name)

            Button(window, text="Enter", command=lambda: New(click.get(),new_file_name.get())).pack()
        def open_a_file(path_passing):
            window = Toplevel()
            window.title('Open A File')
            workfile.geometry('500x500')
            Label(window, text="Enter the file name").pack()
            new_file_name = Entry(window, width=50)
            new_file_name.pack()

            def open_file(path_passing, file_name):
                window.destroy()
                searching(path_passing,file_name)

            Button(window, text="Enter", command=lambda: open_file(path_passing,new_file_name.get())).pack()
        def delete_a_file(path_passing):
            window = Toplevel()
            window.title('Delete A File')
            workfile.geometry('500x500')
            Label(window, text="Enter the file name").pack()
            new_file_name = Entry(window, width=50)
            new_file_name.pack()
            def delete_file(path_passing, file_name):
                window.destroy()
                deleting(path_passing, file_name)
            Button(window, text="Enter", command=lambda: delete_file(path_passing, new_file_name.get())).pack()
        def list_files(path_passing):
            listing(path_passing)
        def copy_file(path_passing):
            window = Toplevel()
            window.title('Copy A File')
            workfile.geometry('500x500')
            Label(window, text="Enter the file name").pack()
            new_file_name = Entry(window, width=50)
            new_file_name.pack()

            def copy_file(path_passing, file_name):
                window.destroy()
                copying(path_passing, file_name)

            Button(window, text="Enter", command=lambda: copy_file(path_passing, new_file_name.get())).pack()
        def move_file(path_passing):
            window = Toplevel()
            window.title('Move A File')
            workfile.geometry('500x500')
            Label(window, text="Enter the file name").pack()
            new_file_name = Entry(window, width=50)
            new_file_name.pack()

            def move_file1(path_passing, file_name):
                window.destroy()
                move_a_file(path_passing,file_name)

            Button(window, text="Enter", command=lambda: move_file1(path_passing, new_file_name.get())).pack()
        def share_on_LAN(path_passing):
            return
        def sort_a_file(path_passing):
            window = Toplevel()
            window.title('sort A File')
            workfile.geometry('500x500')
            click = StringVar()
            click.set('Select the method of sorting')
            drop = OptionMenu(window, click, "size", "date of creation ", "last accessed","last modified")
            drop.pack()
            def sort_file(path_passing,request):
                window.destroy()
                sort_type1(request)
            Button(window, text="Enter", command=lambda: sort_file(path_passing, click.get())).pack()
        def rename_a_file(path_passing):
            window = Toplevel()
            window.title('Rename A File')
            workfile.geometry('500x500')
            Label(window, text="Enter the orignal file name").pack()
            file_name = Entry(window, width=50)
            file_name.pack()
            Label(window, text="Enter the new file name").pack()
            new_file_name = Entry(window, width=50)
            new_file_name.pack()
            def rename_file(path_passing, file_name, new_file_name):
                window.destroy()
                renameing(path_passing, file_name, new_file_name)
            Button(window, text="Enter", command=lambda: rename_file(path_passing, file_name.get(), new_file_name.get())).pack()
        workfile = Toplevel()
        workfile.title('Chose the Work')
        workfile.geometry('500x500')
        workonfile.destroy()

        work_on_file_frame = LabelFrame(workfile, text="Chose The Work To Do", padx=100, pady=100)
        work_on_file_frame.pack(padx=50, pady=50)

        Button(work_on_file_frame, text="sort File by extention").grid(row=0, column=0)
        Button(work_on_file_frame, text="compress using ZIP File", command=lambda: zip_fun1(take_path)).grid(row=1, column=0)
        Button(work_on_file_frame, text="open a file", command= lambda: open_a_file(take_path)).grid(row=2, column=0)
        Button(work_on_file_frame, text="New File", command= lambda: new(take_path)).grid(row=0, column=1)
        Button(work_on_file_frame, text="Sort a File by filestatus", command= lambda: sort_a_file(take_path)).grid(row=1, column=1)
        Button(work_on_file_frame, text="Make a secure Folder", command=lambda: secure_folder(take_path)).grid(row=2, column=1)
        Button(work_on_file_frame, text="delete a file", command= lambda:delete_a_file(take_path)).grid(row=3, column=0)
        Button(work_on_file_frame, text="list all files", command= lambda: list_files(take_path)).grid(row=3, column=1)
        Button(work_on_file_frame, text="copy files to another dirc", command= lambda: copy_file(take_path)).grid(row=4, column=0)
        Button(work_on_file_frame, text="move files to another dirc", command= lambda: move_file(take_path)).grid(row=4, column=1)
        Button(work_on_file_frame, text="share directory on LAN", command= lambda: share_on_LAN(take_path)).grid(row=5, column=0)
        Button(work_on_file_frame, text="Rename a File", command = lambda :rename_a_file(take_path)).grid(row=5, column=1)
        Button(work_on_file_frame, text="BACK",command=workfile.destroy).grid(row=6, column=0)

    # making Toplevel
    workonfile = Toplevel()
    workonfile.title('Working On File')
    workonfile.geometry('400x150')
    if login_status == False:
        messagebox.showwarning('Invalid Access', 'Login to Proceed')
        workonfile.destroy()
    Label(workonfile, text="Open a Directory Path ").pack()
    def open_file():
        workonfile.file_path_dirc = filedialog.askdirectory(initialdir="C:", title="select a file")
        working(workonfile.file_path_dirc)

    Checkbutton(workonfile,text="Remember path").pack()
    Button(workonfile,text="Take recent File").pack()
    Button(workonfile,text="Open",command=open_file).pack()
    #Button(workonfile, text="Enter", command=lambda: working(path)).pack()


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

                Button(uploading, text="Click to Continue", command=first_id).pack()
            else:
                ask_destination = messagebox.askquestion('taking destination', 'change the destination Id?')
                if ask_destination == 'yes':
                    Label(uploading, text="Enter your Drive File ID ").pack()
                    folder_id = Entry(uploading, width=40)
                    folder_id.pack(pady=5)

                    def change_id():
                        main1(str(take_path), str(folder_id.get()), 'upload', "")
                        uploading.destroy()

                    Button(uploading, text="Click to Continue", command=change_id).pack()
                    # uploading.destroy()
                else:
                    # Label(uploading, text=str(fixed_id)+'hii').pack()
                    main1(str(take_path), "", 'upload', "")
                    uploading.destroy()

        def zipping(take_path):
            zipp = Toplevel()
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
                ask_first_time_login = messagebox.askquestion('ask first time',
                                                              'Did you provide destination Folder ID?')
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
                else:
                    main1(str(give_path), "", '', path)
                    uploading.destroy()
                    zipp.destroy()

            Button(zipp, text="Enter", command=lambda: zip_fun(take_path)).pack()

        def list_files(take_path):
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
                    main1(take_path, folder_id.get(), "list_files", "")
                    uploading.destroy()

                Button(uploading, text="Click to Continue", command=first_id).pack()
            else:
                main1(take_path, "", "list_files", "")
                uploading.destroy()

        backup_frame = LabelFrame(backups, text="Create a Backup", padx=100, pady=100)
        backup_frame.pack(padx=50, pady=50)
        Button(backup_frame, text="Upload to Google Drive", command=lambda: upload(path)).pack()
        Button(backup_frame, text="Compress using ZIP & upload", command=lambda: zipping(path)).pack()
        Button(backup_frame, text="Download from Drive").pack()
        Button(backup_frame, text="files in Google Drive backup", command=lambda: list_files(path)).pack()
        Button(backup_frame, text="back to Home Page", command=backups.destroy).pack()

    Label(takingdirc_path, text="Enter the Backup folder Path").pack()
    backup_path = Entry(takingdirc_path, width=50)
    backup_path.pack()
    Button(takingdirc_path, text="Enter", command=lambda: taking_path(backup_path.get())).pack()


def logout():
    messagebox.showinfo('Logging Out', 'Thank You for using File Manager')
    options.destroy()


blog = Button(menu_frame, text="Login", command=loggin).grid(row=0, column=0)
b1 = Button(menu_frame, text="Work on File", command=window31).grid(row=1, column=0)
b2 = Button(menu_frame, text="Make A Backup", command=window32).grid(row=2, column=0)
b3 = Button(menu_frame, text="Log Out", command=logout).grid(row=3, column=0)
options.mainloop()
