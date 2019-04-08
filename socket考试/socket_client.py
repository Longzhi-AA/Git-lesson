import socket
from threading import Thread,RLock
lock1 = RLock()
lock2 = RLock()

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
    print('.......server is connected........')

    send = Thread(target=sendmsg, args=(client,))
    recv = Thread(target=recvmsg, args=(client,))
    lock1.acquire()
    send.start()
    lock1.release()
    lock2.acquire()
    recv.start()
    lock2.release()

    send.join()
    recv.join()


if __name__ == "__main__":
    address = ('127.0.0.1', 8100)
    connect(address)
