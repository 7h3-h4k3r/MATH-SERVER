from subprocess import PIPE , Popen ,STDOUT
p = Popen(['bc'],stdin = PIPE ,stdout = PIPE,stderr = STDOUT)
while p.poll() is None:
    user = input()
    user = user + '\n'
    p.stdin.write(user.encode())
    p.stdin.flush()
    print(p.stdout.readline().decode().strip())