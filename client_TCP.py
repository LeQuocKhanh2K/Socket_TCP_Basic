import socket

def chooServer():
    global SERVER_ADDR
    SERVER_ADDR=input("Choose IP Address Connect: ")
    global PORT
    PORT=int(input("Choose Port Connect: "))

def createClient():
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    soc.connect((SERVER_ADDR, PORT))
    content1=soc.recv(1024).decode()
    print(content1)
    content2="Client Hello Server"
    soc.send(content2.encode())
    soc.close()

if(__name__=="__main__"):
    chooServer()
    createClient()
    