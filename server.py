import socket

HOST = '192.168.0.7'
PORT = 9090

#this socket is for listening / accepting  new connecitons
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
print('server binded')

server.listen(5)

while True:
    #comSocket is for
    comSocket, addr = server.accept()
    print(f"CONNECTION ESTABLISHED WITH: {addr}")

    message = comSocket.recv(1024).decode('utf-8')
    print(f"CLIENT {addr}: {message}")

    comSocket.send(f"SERVER: recieved message".encode('utf-8'))

    comSocket.close()

    print(f"SERVER: connection with {addr}ended")
