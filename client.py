import socket

HOST = '192.168.0.7'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((HOST, PORT))

socket.send('hello from the client'.encode('utf-8'))

print(socket.recv(1024).decode('utf-8'))
