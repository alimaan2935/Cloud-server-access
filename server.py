import socket

def Main():
    host = '130.211.148.164'
    port = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(1)

    c, address = s.accept()

    print("Connection from " + str(address))

    while True:
        data = c.recv(1024)
        if not data:
            break
        print("From connected user " + str(data))
        data = str(data).upper()
        print("Sending " + str(data))
        c.send(bytes(data, encoding="UTF-8"))

    c.close()

if __name__ == '__main__':
    Main()