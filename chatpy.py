import socket

type = input("Введите тип: ")

if type == 's':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 2000))
    server.listen()

    user, adres = server.accept()
    print("connect")

    while True:


        user.send(input().encode("utf-8"))

        data = user.recv(1024)
        print(data.decode("utf-8"))


elif type == 'c':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("127.0.0.1", 2000))

    while True:
        data = client.recv(1024)
        print(data.decode("utf-8"))

        client.send(input().encode("utf-8"))


