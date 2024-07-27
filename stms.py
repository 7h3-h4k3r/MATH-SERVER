#STMS = Sokcet thread math server
import socket
from subprocess import PIPE ,STDOUT ,Popen
import threading
class Math_thread_stdout(threading.Thread):
    def __init__(self,proc,conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.proc = proc
    def run(self):
        while not self.proc.stdout.closed:
            try:
                self.conn.sendall(self.proc.stdout.readline())
            except:
                pass
class Math_thread_stdin(threading.Thread):
    def __init__(self,conn,add):
        threading.Thread.__init__(self)
        self.conn = conn
        self.add = add
    def run(self):
        print("incoming connection {}_{}".format(self.add[0],self.add[1]))
        self.conn.sendall("Simple lightWight Math server :2024 version:0.1 \n Made by Sridharanitharan.B \n".encode())
        bc_proc = Popen(['bc'],stdin = PIPE,stdout= PIPE,stderr = STDOUT)
        start_ = Math_thread_stdout(bc_proc,self.conn)
        start_.start()
        while bc_proc.poll() is None:
            try:
                data = self.conn.recv(1024)
                if not data:
                    break
                data = data.decode().strip()
                query =  data + '\n'
                bc_proc.stdin.write(query.encode())
                bc_proc.stdin.flush()
            except:
                pass
HOST = ''
PORT = 9090
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST,PORT))
server.listen()
print("listing port is........{}",PORT)
while True:
    conn , add = server.accept()
    start_ = Math_thread_stdin(conn,add)
    start_.start()
server.closed