#STMS = Sokcet thread math server
import socket
from subprocess import PIPE ,STDOUT ,Popen
import threading
import re
import time
conn_count=[]
# pattern = r"([0-9]{1,4}[\+\-\*\^/][0-9]{1,4})|([a-z]\s*[\+\-\*\^\=/]\s*[0-9]{1,4})" 
pattern = r"([0-9]{1,4}\s*==\s*[0-9]{1,4})|([0-9]{1,4}\s*[\+\-\*\<\>\^\=/]\s*[0-9]{1,4})|([a-z]+\s*[\+\-\*\<\>\^\=/]\s*[0-9]{1,4})|([a-z]+\s*[\+\-\*\<\>\^\=/]\s*[a-z]+)|([a-z]+\s*==\s*[a-z]+)"# #update is not end(add some update in feture)
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
    def Count_MilliSec(self):
        return round(time.time())
    def run(self):
        try:
            self.conn.sendall("Simple lightWight Math server :2024 version:0.2 \n Made by Sridharanitharan.B \n".encode())
            print("Incoming connection :{}-{}".format(add[0],add[1]))
            #APPLICATION LAYER (7)
            bc_proc = Popen(['bc'],stdin = PIPE,stdout= PIPE,stderr = STDOUT)
            start_ = Math_thread_stdout(bc_proc,self.conn)
            start_.start()
            while bc_proc.poll() is None:
                warning = 1
                try:#PRESENTATION LAYER(6)
                    st = self.Count_MilliSec()
                    data = self.conn.recv(1024)
                    en = self.Count_MilliSec()
                    FinalTime = en-st
                    if(FinalTime>=1):
                        if not data:
                            break
                        data = data.decode().strip()
                        #print(data) feture usage
                        u_filter = re.match(pattern,data)
                        if u_filter:
                            query =  data + '\n'
                            bc_proc.stdin.write(query.encode())
                            bc_proc.stdin.flush()
                        else:
                            self.conn.send("(*) Invaild systax \n".encode())
                    else:
                        self.conn.sendall("[*] connection has been failed\n".encode())
                        break
                            
                        self.conn.close()   
                except:
                    break
                    
        except:
            pass
HOST = ''
PORT = 8989
#SESSION LAYER(5)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST,PORT))
server.listen()
print("listing port is........{}",PORT)
while True:
    conn , add = server.accept()
    try:
        for address in conn_count:
            if address in add[0]:
                conn_count.remove(add[0])
                conn.send("[*] Already your Service in Online ".encode())
                conn.close()
                break
        conn_count.append(add[0])
    except:
        break
    
    start_ = Math_thread_stdin(conn,add)
    start_.start()
server.closed()
