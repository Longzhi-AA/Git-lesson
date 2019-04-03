import socket
from threading import Thread


def connect(address):
    client = socket.socket()
    client.connect(address)
    print('.......server connected........')

    while 1:
        try:
            msg = input('please input:')
            client.send(msg.encode())
        except Exception:
            client.close()
            break


if __name__ == "__main__":
    address = ('127.0.0.1', 8080)
    tk = Thread(target=connect,args=(address,))
    tk.start()
