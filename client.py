import socket 
import threading 
def msg(clint):
    buffer=""
    while True:
        data = clint.recv(10*10240)
        if data:
            buffer+=data.decode()
            if buffer.endswith("\n"):
                print(buffer.strip())
                buffer=""
    
host ="127.0.0.1"
port = 7070
clint = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clint.connect((host,port))
while True:
        th =threading.Thread(target= msg,args=(clint,))
        th.start()
        message = input()
        clint.send(message.encode())

       

