import socket
import os


def chat():
    try:

        type = input("Введите тип: ")
#server
        if type == 's':

            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1", 2000))
            server.listen()

            user, adres = server.accept()
            print("connect")

            str = input()

            while True:
                user.send(str.encode("utf-8"))

                data = user.recv(1024)
                print(data.decode("utf-8"))
#client
        elif type == 'c':
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client.connect(("127.0.0.1", 2000))

            while True:
                data = client.recv(1024)
                print(data.decode("utf-8"))

                client.send(input().encode("utf-8"))

        else:
            print("ERROR")
            os.system("pause")

    except:
        print("ERROR")
        os.system("pause")


def main():
    chat()


main()


