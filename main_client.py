import socket
import tqdm
import os
def client_connect(host_ip,port_no,file_path):
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
    # the ip address or hostname of the server, the receiver
    host = host_ip
    # the port, let's use 5001
    port = int(port_no)
    # the name of file we want to send, make sure it exists
    filename = file_path
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
    with open(filename, "rb") as f:
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

'''def connecting_client(file_path):
    is_file = file_path.split('.')
    if(len(is_file)==1):
        for files in os.listdir(file_path):

    else:
        print(is_file)
        print(file_path)

connecting_client('C:/Users/91922/Desktop/hllu')'''

