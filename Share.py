import sqlite3
from tkinter import *
from tkinter import messagebox
from database import *
from main_client import *
from main_server import *
def Share(file_path):
    root = Tk()
    root.title("Share on LAN")
    root.resizable()
    # textfield
    def insert_database():
            root1 = Toplevel()
            root1.title('New Connection')
            Label(root1, text="User Name :-- ").grid(row=0, column=0)
            user_name = Entry(root1, width=50)
            user_name.grid(row=0, column=1)
            Label(root1, text="Port number :-- ").grid(row=1, column=0)
            port_no = Entry(root1, width=50)
            port_no.grid(row=1, column=1)
            Label(root1, text="Host IP :-- ").grid(row=2, column=0)
            host_ip = Entry(root1, width=50)
            host_ip.grid(row=2, column=1)

            def connect():
                put_in_database(user_name.get(), port_no.get(), host_ip.get(), "Insert")
                root1.destroy()

            Button(root1, text="Enter",fg="white" , bg="gray" , font="aerial 12 bold" , relief="raised", command=connect).grid(row=3, columnspan=2)
    def delete_database():
            root1 = tk.Toplevel()
            root1.title('Delete a Connections')
            record = put_in_database("","","","display")
            if(record == []):
                root1.destroy()
            else:
                tk.Label(root1, text="Select the connection to remove").pack()
                clicked = StringVar()
                clicked.set('Select')
                option_list = []
                for records in record:
                    option_list.append(records[0])
                tk.OptionMenu(root1, clicked, *option_list).pack()
                def deleting():
                    print(clicked.get())
                    put_in_database("", "", clicked.get(), "delete")
                    root1.destroy()
                tk.Button(root1, text="Enter",fg="white" , bg="gray" , font="aerial 12 bold" , relief="raised", command=deleting).pack()
    def display_database():
            root1 = Toplevel()
            root1.title('Display the Connections')
            record = put_in_database("", "", "", "display")
            table =""
            if (record == []):
                root1.destroy()
            for records in record:
                table = table +"\n \t"+ str(records)
            tk.Label(root1, text="ip Address").grid(row=0, column=1)
            tk.Label(root1, text="host Name").grid(row=0, column=2)
            tk.Label(root1, text="port").grid(row=0, column=3)
            tk.Label(root1, text=table).grid(row=1, columnspan=3)
            tk.Button(root1, text="OK",fg="white" , bg="gray" , font="aerial 12 bold" , relief="raised", command=root1.destroy).grid(row=2, columnspan=3)
    def connect_connection():
            root_window = Toplevel()
            root_window.title("helllo there")
            root_window.resizable()
            r = put_in_database("", "", "", "display")

            host_ip = StringVar()
            host_ip.set('select the connection')
            user_name = StringVar()
            user_name.set('select the connection')
            port_no = StringVar()
            port_no.set('select the connection')
            Label(root_window, text="host ip :-- ").grid(row=0, column=0)
            Label(root_window, textvariable=host_ip).grid(row=0, column=1)
            Label(root_window, text="user name :-- ").grid(row=1, column=0)
            Label(root_window, textvariable=user_name).grid(row=1, column=1)
            Label(root_window, text="port no :-- ").grid(row=2, column=0)
            Label(root_window, textvariable=port_no).grid(row=2, column=1)
            global connection_no
            connection_no = -1
            if r == []:
                messagebox.showinfo('Display the connection', 'No connections found')
                root_window.destroy()

            def next(no):
                if no < 0:
                    host_ip.set('select the connection')
                    user_name.set('select the connection')
                    port_no.set('select the connection')
                else:
                    host_ip.set(r[no][0])
                    user_name.set(r[no][1])
                    port_no.set(r[no][2])

            def prev(no):
                if no < 0:
                    host_ip.set('select the connection')
                    user_name.set('select the connection')
                    port_no.set('select the connection')
                else:
                    host_ip.set(r[no][0])
                    user_name.set(r[no + 1][1])
                    port_no.set(r[no][2])

            def connect():
                root1 = Toplevel()
                root1.title('Connecting')
                root1.resizable()
                root_window.destroy()
                def sending():
                    client_connect(host_ip.get(),port_no.get(),file_path)

                def receving():
                    server_connect(host_ip.get(),port_no.get())

                Button(root1, text="SEND",fg="white" , bg="gray" , font="aerial 12 bold" , relief="raised", command=lambda: sending()).pack()
                Button(root1, text="RECEIVE",fg="white" , bg="gray" , font="aerial 12 bold" , relief="raised", command=lambda: receving()).pack()

            def increment():
                global connection_no
                if (connection_no > len(r)):
                    connection_no = -1
                    return connection_no
                else:
                    connection_no = connection_no + 1
                    return connection_no

            def decrement():
                global connection_no
                if (connection_no < 0):
                    connection_no = 1
                    return connection_no
                else:
                    connection_no = connection_no - 1
                    return connection_no

            Button(root_window, text="prev",fg="white" , bg="purple", font="aerial 12 bold" , command=lambda: prev(decrement())).grid(row=3, column=0)
            Button(root_window, text="connect",fg="white" , bg="purple" , font="aerial 12 bold", command=lambda: connect()).grid(row=3, column=1)
            Button(root_window, text="next",fg="white" , bg="purple" , font="aerial 12 bold", command=lambda: next(increment())).grid(row=3, column=2)
            Button(root_window, text="BACK",fg="white" , bg="gray", font="aerial 12 bold", command=root_window.destroy).grid(row=4, column=1)
    Button(root, text="New connection",fg="white" , bg="purple" , font="aerial 12 bold" ,padx=21, relief="raised",command=insert_database).pack()
    Button(root, text="connect",fg="white" , bg="purple" , font="aerial 12 bold" , relief="raised",padx=52,command=connect_connection).pack()
    Button(root, text="Delete connection",fg="white" , bg="purple", font="aerial 12 bold" , relief="raised",padx=14, command=delete_database).pack()
    Button(root, text="Display  Connections",fg="white" , bg="purple" , font="aerial 12 bold" , relief="raised", command=display_database).pack()
    Button(root, text="BACK",fg="white" , bg="gray" , font="aerial 12 bold" , relief="raised",padx=59, command=root.destroy).pack()
    root.mainloop()


