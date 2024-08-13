import socket 
import threading 
def msg(client):
    data = client.recv(10*10240)
    if data:
        print("length of data {}".format(len(data)))
        print(data.decode().strip())
    
host ="127.0.0.1"
port = 7070
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
while True:
        th =threading.Thread(target= msg,args=(client,))
        th.start()
        message = input()
        client.send(message.encode())
