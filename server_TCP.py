import socket

def getInfo():
    global HOST_NAME
    HOST_NAME=socket.gethostname()
    global HOST_ADDR
    HOST_ADDR=socket.gethostbyname(HOST_NAME)
    print(HOST_NAME)
    print(HOST_ADDR)

def choosePort():
    global PORT
    PORT=int(input("Choose Port Connect: "))

def createServer():
    soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.bind((HOST_ADDR, PORT))
    soc.listen(5)
    while True:
        clientConnect, clientAddr=soc.accept()
        print("Connect to Client: ",clientAddr)
        content1="Server hello Client"
        clientConnect.send(content1.encode())
        content2=clientConnect.recv(1024).decode()
        print(content2)

if(__name__=="__main__"):
    getInfo()
    choosePort()
    createServer()