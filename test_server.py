import socket
Headersize = 10
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),5421))
s.listen(5)
while True:
    clientsocket,address = s.accept()
    print(f'Connection from {address} has started')
    clientsocket.send(bytes("welcome to server its ME ",'utf-8'))