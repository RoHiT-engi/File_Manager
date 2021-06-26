import os
from tkinter import *
from tkinter import messagebox
from Drive import *
from compress_using_zip import *
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
from Share import *
from unzip_a_file import *
from Rename_a_file import *
from zip_a_file import *
from making_db import *

options = Tk()
options.title("Home Page")
# options frame
menu_frame = LabelFrame(options, text="Chose The Following", padx=100, pady=100)
menu_frame.pack(padx=50, pady=50)
global login_ID
login_status = False

def loggin():
    # loggin window
    login = Toplevel()
    login.title('File Manager & Recovery System')
    login.geometry('500x500')
    global login_text_field
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
        pwd_check=put_in_back('login',login_text_field.get(),'','','')
        print(pwd_check)
        # making login_status
        if (pwd_check==[]):
            messagebox.showwarning('Login status','Invalid login ID or password')
        if (pass_text_field.get() == pwd_check[0][0]):
            global login_status
            global login_ID
            login_ID = login_text_field.get()
            login_status = True
            messagebox.showinfo('Login_status','Successfull login')
            login.destroy()

    Button(login_frame, text="Enter", command=logging).grid(row=3, columnspan=2)



def window31():
    # work on file
    def working(take_path):
        take_path1=take_path
        def zip_fun1(path_passing):
            zipp1 = Toplevel()
            zipp1.title('Make a ZIP file')
            zipp1.geometry('400x100')
            Label(zipp1, text="Enter ZIP File Name").pack()
            file_name = Entry(zipp1, width=50)
            file_name.pack(pady=5)
            def zipping(take_path):
                zip(str(file_name.get()),'compress_dirc',take_path)
                zipp1.destroy()
            Button(zipp1, text="Enter", command=lambda: zipping(path_passing)).pack()
        def secure_folder():
            zipp1 = Toplevel()
            zipp1.title('Make a Secure file')
            zipp1.geometry('400x100')
            messagebox.showinfo('Open file','select the secure file')
            path_passing = filedialog.askdirectory(initialdir="C:/desktop", title="select a directory")
            Label(zipp1, text="Enter Secure Folder Name").pack()
            file_name = Entry(zipp1, width=50)
            file_name.pack(pady=5)
            def things_to_do(file_name):
                encrypt = Toplevel()
                zipp1.destroy()
                encrypt.title('Making a secure folder')
                path=zip(file_name,'compress_dirc',path_passing)
                def open_encrypted():
                    try :
                        os.startfile('your_encrypted_file.encrypted')
                    except FileNotFoundError :
                        messagebox.showinfo('encryption Status','you have not encrypted the file')
                Button(encrypt, text="encrypt the file", command=lambda: encrypting(path)).pack()
                Button(encrypt, text="decrypt the file", command=lambda: decrypting(path)).pack()
                Button(encrypt, text="open the encrypted file", command=open_encrypted).pack()
            Button(zipp1, text="Enter", command=lambda: things_to_do(file_name.get())).pack()
        def sort_by_ext(path_passing):
            window = Toplevel()
            window.title('Sort File By Extention')
            workfile.geometry('500x500')
            click = StringVar()
            click.set('Select the Extention')
            drop = OptionMenu(window, click, "txt", "mp3", "mp4", "pptx", "jpg", "jpeg", "png", "doc", "docx", "pdf")
            drop.pack()
            def sort(clicked_val):
                window.destroy()
                sort_using_extention(path_passing,clicked_val)
                messagebox.showinfo('sort Status','Sorted succesfully')

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
            Share(path_passing)
        def sort_a_file(path_passing):
            window = Toplevel()
            window.title('sort A File')
            workfile.geometry('500x500')
            click = StringVar()
            click.set('Select the method of sorting')
            drop = OptionMenu(window, click, "file size", "file Name","last modified")
            drop.pack()
            def sort_file(path_passing,request):
                window.destroy()
                sort_type1(request,path_passing)
            Button(window, text="Enter", command=lambda: sort_file(path_passing, click.get())).pack()
        def unzip_file(path_passing):
            check=messagebox.askyesno('UNZIPPING','do you want to keep original ZIP file after extraction')
            unzip(check)
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
        def change_path(path_passing):
            path2 = filedialog.askdirectory(initialdir="C:/desktop", title="select a directory to save")
            messagebox.showinfo('hi', f'your working directory {path_passing} has changed to {path2}')
            put_in_back('put_prev_path', login_ID, path2, '','')
            working(path2)
            workfile.destroy()
        def zip_a_folder():
            zipp1 = Toplevel()
            zipp1.title('Make a ZIP file')
            zipp1.geometry('400x100')
            Label(zipp1, text="Enter ZIP File Name").pack()
            file_name = Entry(zipp1, width=50)
            file_name.pack(pady=5)
            def zipping():
                zip(str(file_name.get()),'','')
                zipp1.destroy()
            Button(zipp1, text="Enter", command= zipping).pack()
        workfile = Toplevel()
        workfile.title('Chose the Work')
        workfile.geometry('500x500')
        workonfile.destroy()

        work_on_file_frame = LabelFrame(workfile, text="Chose The Work To Do", padx=100, pady=100)
        work_on_file_frame.pack(padx=50, pady=50)

        Button(work_on_file_frame, text="sort File by extention",command = lambda:sort_by_ext(take_path)).grid(row=0, column=0)
        Button(work_on_file_frame, text="compress folder using ZIP", command=lambda: zip_fun1(take_path)).grid(row=1, column=0)
        Button(work_on_file_frame, text="open a file", command= lambda: open_a_file(take_path)).grid(row=2, column=0)
        Button(work_on_file_frame, text="New File", command= lambda: new(take_path)).grid(row=0, column=1)
        Button(work_on_file_frame, text="Sort a File by filestatus", command= lambda: sort_a_file(take_path)).grid(row=1, column=1)
        Button(work_on_file_frame, text="Make a secure Folder", command=secure_folder).grid(row=2, column=1)
        Button(work_on_file_frame, text="delete a file", command= lambda:delete_a_file(take_path)).grid(row=3, column=0)
        Button(work_on_file_frame, text="list all files", command= lambda: list_files(take_path1)).grid(row=3, column=1)
        Button(work_on_file_frame, text="copy files to another dirc", command= lambda: copy_file(take_path)).grid(row=4, column=0)
        Button(work_on_file_frame, text="move files to another dirc", command= lambda: move_file(take_path)).grid(row=4, column=1)
        Button(work_on_file_frame, text="share directory on LAN", command= lambda: share_on_LAN(take_path)).grid(row=5, column=0)
        Button(work_on_file_frame, text="Rename a File", command = lambda :rename_a_file(take_path)).grid(row=5, column=1)
        Button(work_on_file_frame, text="unzip a File", command=lambda :unzip_file(take_path)).grid(row=6,column=1)
        Button(work_on_file_frame, text="BACK",command=workfile.destroy).grid(row=6, column=0)
        Button(work_on_file_frame, text="ZIP a file",command= zip_a_folder).grid(row=7, column=1)
        Button(work_on_file_frame, text="Change Directory", command=lambda :change_path(take_path)).grid(row=7, column=0)
        Button(work_on_file_frame, text="Compress a file").grid(row=8,column=0)
    # making Toplevel
    workonfile = Toplevel()
    workonfile.title('Working On File')
    workonfile.geometry('400x150')
    if login_status == False:
        messagebox.showwarning('Invalid Access', 'Login to Proceed')
        workonfile.destroy()
    else:
        check=messagebox.askyesno('Prev folder','whould you like to continue with previous directory')
        if (check==True):
            prev_path=put_in_back('work_on_file',login_ID,'','','')
            if(prev_path == []):
                messagebox.showinfo('Work on file status','no previous directory found')
                messagebox.showinfo('Open', 'chose your working directory')
                workonfile.file_path_dirc = filedialog.askdirectory(initialdir="C:/desktop", title="select a directory")
                put_in_back('put_prev_path', login_ID, workonfile.file_path_dirc, '','')
                working(workonfile.file_path_dirc)
            else:
                working(prev_path[0][0])
        else:
            messagebox.showinfo('Open','chose your working directory')
            workonfile.file_path_dirc = filedialog.askdirectory(initialdir="C:/desktop", title="select a directory")
            put_in_back('put_prev_path',login_ID,workonfile.file_path_dirc,'','')
            working(workonfile.file_path_dirc)



def window32():
    # create Backup
    # making top level
    takingdirc_path = Toplevel()
    takingdirc_path.title("Taking Path")
    takingdirc_path.geometry('400x100')
    if login_status == False:
        messagebox.showwarning('Invalid Access', 'Login to Proceed')
        takingdirc_path.destroy()
    else:
        messagebox.showinfo('Open', 'chose your backup folder')
        takingdirc_path.file_path_dirc = filedialog.askdirectory(initialdir="C:/desktop", title="select a directory")
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
                record = put_in_back('get_folder_id', login_ID, '','','')
                def new_folder_id():
                    Label(uploading, text="enter the folder id").pack()
                    folder_id = Entry(uploading, width=40)
                    folder_id.pack()
                    put_in_back('put_folder_id', login_ID, '', '', folder_id.get())
                    def upload_to_drive(folder_id, pathpassing):
                        main1(pathpassing, folder_id, 'upload', '')
                        uploading.destroy()
                    Button(uploading, text="Enter", command=lambda: upload_to_drive(folder_id.get(), take_path)).pack()
                if(record == []):
                    messagebox.showinfo('take Folder ID','Plz provide your destination folder of google drive')
                    new_folder_id()
                else:
                    check=messagebox.askyesno('Change Folder ID','do you want to change the Folder ID')
                    if(check == True):
                        new_folder_id()
                    else:
                        print(record[0][0])



            def zipping(take_path):
                zipp = Toplevel()
                zipp.title("zip a file")
                zipp.geometry('400x250')
                Label(zipp, text="Enter ZIP File Name").pack()
                file_name = Entry(zipp, width=50)
                file_name.pack(pady=5)

                def zip_fun(path_passing):
                    zip(str(file_name.get()), 'compress_dirc', path_passing)
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
                    main1(take_path, "", "list_files",login_ID )
                    uploading.destroy()

            backup_frame = LabelFrame(backups, text="Create a Backup", padx=100, pady=100)
            backup_frame.pack(padx=50, pady=50)
            Button(backup_frame, text="Upload to Google Drive", command=lambda: upload(path)).pack()
            Button(backup_frame, text="Compress using ZIP & upload", command=lambda: zipping(path)).pack()
            Button(backup_frame, text="Download from Drive").pack()
            Button(backup_frame, text="files in Google Drive backup", command=lambda: list_files(path)).pack()
            Button(backup_frame, text="back to Home Page", command=backups.destroy).pack()
        taking_path(takingdirc_path.file_path_dirc)


def logout():
    messagebox.showinfo('Logging Out', 'Thank You for using File Manager')
    options.quit()

def admin_access():
    return

Button(menu_frame, text="Login", command=loggin).grid(row=0, column=0)
Button(menu_frame, text="Work on File", command=window31).grid(row=1, column=0)
Button(menu_frame, text="Make A Backup", command=window32).grid(row=2, column=0)
Button(menu_frame, text="Log Out", command=logout).grid(row=3, column=0)
options.mainloop()