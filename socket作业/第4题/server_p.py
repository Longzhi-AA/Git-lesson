import socket
from threading import Thread


def server_connect(address):
    ss = socket.socket()
    ss.bind(address)
    ss.listen(1)
    print('<-------server started------>')

    try:
        conn, addr = ss.accept()
        print('{} connected'.format(addr))

        while 1:

            msg = conn.recv(65535)
            if not msg:
                break
            print('来自{}的消息：{}'.format(addr[0], msg.decode()))
    except Exception:
        ss.close()
        print('connection lost')



if __name__ == "__main__":
    address = ('127.0.0.1', 8080)
    tk = Thread(target=server_connect, args=(address,))
    tk.start()