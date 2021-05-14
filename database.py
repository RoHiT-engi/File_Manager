import sqlite3
from tkinter import messagebox as mb
import tkinter as tk
def put_in_database(user_name,port_no,host_IP,request):
    #create a database or connect to one
    conn=sqlite3.connect('LAN_database.db')
    #create cursor
    c = conn.cursor()
    #execute commands
    if(request == "Insert"):
        c.execute("INSERT INTO connection VALUES(:host_ip, :user_name, :port_no)",
                {
                'host_ip': host_IP,
                'user_name':user_name,
                'port_no':port_no
                })
        mb.showinfo('Inserted', 'succescfull')
    elif (request == "delete"):
        print(host_IP)
        try :
            c.execute(f"DELETE FROM connection WHERE host_ip = '{host_IP}'")
        except sqlite3.OperationalError:
            mb.showinfo('Connecting','NO CONNECTION FOUND')
        mb.showinfo('Deleting', 'succescfull')
    elif (request == "display"):
        try:
            c.execute("SELECT * FROM connection")
        except sqlite3.OperationalError:
            mb.showinfo('Connecting','NO CONNECTION FOUND')
        record = c.fetchall()
        return record
    #commit changes
    conn.commit()
    #close connection
    conn.close()

