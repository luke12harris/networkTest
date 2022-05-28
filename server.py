import socket
import _thread
import threading

printLock = threading.Lock()


def threaded (comSock):

    while True:
        data = comSock.recv(1024)
        if not data:
            print("not cool")
            printLock.release()
            break

        data = data[::1] #reverse the incoming data

        comSock.send(data)
    comSock.close()


def main():
    HOST = '192.168.0.9'
    PORT = 9090

    #this socket is for listening / accepting  new connecitons
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSock.bind((HOST, PORT))
    print('server binded')

    serverSock.listen(5)
    print("server is listening")

    while True:
        #comSock is a communication socket
        comSock, addr = serverSock.accept()

        printLock.acquire()

        print(f"connection with {addr[0]}:{addr[1]}")

        _thread.start_new_thread(threaded, (comSock,))

    serverSock.close()


if __name__ == "__main__":
    main()
