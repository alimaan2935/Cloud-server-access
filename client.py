import socket

def Main():
    host = '130.211.148.164'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("Enter stuff here --> ")

    while message != 'q':
        s.send(bytes(message, encoding="UTF-8"))
        data = s.recv(1024)
        print("Recieved from server: " + str(data))

        message = input(" --> ")

    s.close()


if __name__ == '__main__':
    Main()
