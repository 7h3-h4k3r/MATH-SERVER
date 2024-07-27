import threading
from subprocess import PIPE,Popen,STDOUT
def thread_(p):
    while not p.stdout.closed:
        try:
            print(p.stdout.readline().decode().strip())
        except:
            pass
    # while p.poll is None:
    #     try:
    #         print(p.stdout.readline().decode().strip())
    #     except:
    #         pass

p = Popen(['bc'],stdin = PIPE ,stdout = PIPE ,stderr =STDOUT)
thr = threading.Thread(target=thread_,args=(p,))
thr.start()
while p.poll() is None:
    user_input = input()
    user_input =  user_input + '\n'
    p.stdin.write(user_input.encode())
    p.stdin.flush()

