import socket
from threading import Thread
connlist = list()

def server_recv(conn,addr):
    while 1:

        msg = conn.recv(65535)
        if not msg:
            break
        showmsg = '来自{}的消息：{}'.format(addr[0], msg.decode())
        print(showmsg)
        for connmsg in connlist:
            # print(connmsg)
            connmsg.send(showmsg.encode())

def server_connect(address):
    ss = socket.socket()
    ss.bind(address)
    ss.listen(100)
    print('<-------server started------>')

    while 1:
        try:
            conn, addr = ss.accept()
            connlist.append(conn)
            print('{} connected'.format(addr))
            tk = Thread(target=server_recv, args=(conn,addr))
            tk.start()

        except Exception:
            ss.close()
            print('connection lost')



if __name__ == "__main__":
    address = ('127.0.0.1', 8087)
    server_connect(address)