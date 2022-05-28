import socket

def main();
    HOST = '192.168.0.9'
    PORT = 9090

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.connect((HOST, PORT))

    while True:
        message = input("Enter message to send: ")
        socket.send(message.encode('utf-8'))

        data = socket.recv(1024)

        print(f"Server recieved: {str(data.decode('utf-8'))} ")

        reply = input("Reply? 0/1")
        if reply = 0:
            break
    socket.close

    input()

if __name__ =="__main__":
    main()
