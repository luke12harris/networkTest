import socket

def main():
    HOST = '192.168.0.9'
    PORT = 9090

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect((HOST, PORT))

    while True:
        message = input("Enter message to send: ")

        clientSocket.send(message.encode('utf-8'))

        data = clientSocket.recv(1024)

        print(f"Server recieved: {str(data.decode('utf-8'))} ")

        reply = input("Reply? 0/1")
        if reply == "0":
            break
    clientSocket.close

    input()

if __name__ =="__main__":
    main()
