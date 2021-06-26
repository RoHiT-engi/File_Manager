import socket
from tkinter import filedialog

import tqdm
import os
def client_connect(host_ip,port_no,file_path):
    file=filedialog.askopenfilename(initialdir=file_path, title="select a file", filetypes=(("All files", "*.*"),))
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
    # the ip address or hostname of the server, the receiver
    host = host_ip
    # the port, let's use 5001
    port = int(port_no)
    # the name of file we want to send, make sure it exists
    filename = file
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"Connecting to {host}:{port}")
    s.connect((host, port))
    print("Connected.")
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(rf'{filename}', "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
#client_connect('192.168.0.104',3651,'C:/Users/91922/Desktop/proj')


