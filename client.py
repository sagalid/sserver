import socket
import sys

if (len(sys.argv) > 3):
    serverIp = sys.argv[1]
    port = int(sys.argv[2])
    fileToSend = sys.argv[3]

else:
    print("\n\n Run like \n python3 client.py <server_IP> <port> <file>\n\n")
    exit(1)

s = socket.socket()
s.connect((serverIp, port))
file = open(fileToSend, "rb")
SendData = file.read(1024)


while SendData:
    print(s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)

s.close()
