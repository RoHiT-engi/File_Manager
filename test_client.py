import socket
Headersize = 10
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),5421))
msg = s.recv(1024)
print(msg.decode("utf-8"))