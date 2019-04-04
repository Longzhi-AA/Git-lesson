import socket
from threading import Thread

def sendmsg(client):
    while 1:
        msg = input('please input:')
        try:

            client.send(msg.encode())
        except Exception:
            client.close()
            break

def recvmsg(client):
    while 1:
        try:
            msg = client.recv(65535)
            if not msg:
                break
            print(msg.decode())
        except Exception:
            client.close()
            break

def connect(address):
    client = socket.socket()
    client.connect(address)
    print('.......server connected........')

    send = Thread(target=sendmsg,args=(client,))
    recv = Thread(target=recvmsg,args=(client,))
    send.start()
    recv.start()

    send.join()
    recv.join()


if __name__ == "__main__":
    address = ('127.0.0.1', 8087)
    connect(address)
