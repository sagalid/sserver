import socket
import sys
import uuid

if len(sys.argv) > 2:
    serverIp = sys.argv[1]
    port = int(sys.argv[2])
else:
    print(f"\n\n Run Like \n python3 {sys.argv[0]} <server_IP> <port>\n\n")
    exit(1)

s = socket.socket()
print(f"\n Server is listing on port : {port} \n")
s.bind((serverIp, port))
s.listen(10)
while True:
    file = open(str(uuid.uuid4()), "wb") 
    conn, addr = s.accept()
    conn.send("ping 1.1.1.1".encode("UTF-8"))
    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)
    file.close()
    print("\n File has been copied successfully \n")

    #conn.close()
    print("\n Server closed the connection \n")

    #break
