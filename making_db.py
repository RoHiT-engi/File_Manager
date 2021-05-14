import sqlite3
from tkinter import messagebox as mb
import tkinter as tk
def put_in_back(request,login_id,prev_path,login_pwd):
    #create a database or connect to one
    conn=sqlite3.connect('file_manager.db')
    #create cursor
    c = conn.cursor()
    #execute commands
    if (request == "login"):
        try :
                c.execute(f"SELECT login_pwd FROM login where login_id = '{login_id}'")
                record_login = c.fetchall()
                return record_login
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)
            mb.showerror('Login status','Invalid login ID')
    if (request == "work_on_file"):
        try :
            c.execute(f"SELECT last_working_directory FROM work_file where login_id = '{login_id}'")
            record_work_file = c.fetchall()
            return record_work_file
        except sqlite3.OperationalError:
            mb.showinfo('Last directory','No last used directory found')
    if (request == "put_prev_path"):
        try:
            c.execute(f"INSERT OR REPLACE INTO work_file(last_working_directory,login_ID) VALUES('{prev_path}','{login_id}')")
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)
    if (request == "add_login_id"):
        try:
            c.execute("INSERT OR IGNORE INTO login VALUES(:login_ID, :login_pwd)",
                      {
                          'login_ID': login_id,
                          'login_pwd': login_pwd
                      })
        except sqlite3.OperationalError:
            print(sqlite3.OperationalError)
    if(request == "update_pwd"):
            try:
                c.execute(f"UPDATE login set login_pwd = '{login_pwd}' WHERE login_ID= '{login_id}'")
            except sqlite3.OperationalError:
                print(sqlite3.OperationalError)


    #commit changes
    conn.commit()
    #close connection
    conn.close()

