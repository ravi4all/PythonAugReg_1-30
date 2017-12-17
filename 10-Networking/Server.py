import socket
import threading


def Main():
    host = ""
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Server started on",port)
    print("Waiting for connections...")

    mySocket.listen(5)
    while True:
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        if not data:
            break
        print ("from connected  user: " + str(data))

        myMsg = input("Enter your message : ")
        conn.send(myMsg.encode())

    conn.close()

if __name__ == '__main__':
    thread = threading.Thread(target=Main)
    thread.start()
