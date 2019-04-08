# P1901socket编程试题(考试时2
# 小时):题目: 实现一个多人聊天室要求:
# 1.至少实现一个服务端客户端(C / S模式)的聊天室服务端和客户端代码(0 - 40分)
# 2.能够进行多人同时和服务器收发消息的服务端和客户端代码(40 - 60分)
# 3.能够实现多人同时和服务器收发消息, 并且服务器会广播消息的服务端和客户端代码(60 - 70分)
# 4.能够使用线程池来实现上面功能(70 - 80分)
# 5.能够在完成4要求的情况下考虑到多线程切换的问题, 并且对合适的地方上锁, 并说明为什么要上锁(80 - 90分)
# 6.能够在完成5的要求下实现客户端能顺利关闭退出, 并且其他客户端能收到有客户端退出的消息, 并且整体代码无bug(90 - 100分)
#
# 提交方式: 将代码发至我微信
# 作弊判断规则: 若出现多人代码样视为作弊, 多人全部0分

from concurrent.futures import ThreadPoolExecutor
from functools import partial
import socket
from threading import Lock

connlist = list()
lock = Lock()
pools = ThreadPoolExecutor(max_workers=20)


def server_recv(conn, addr):
    while 1:

        msg = conn.recv(65535)
        if not msg:
            break
        showmsg = '来自{}的消息：{}'.format(addr[0], msg.decode())
        print(showmsg)
        conns(showmsg)


def conns(showmsg):
    if connlist is None:
        print('-----waiting for a new connection -----')
    for conn in connlist:
        try:
            conn.send(showmsg.encode())
        except:
            connlist.remove(conn)
            newmsg = '{} connection lost'.format(conn)
            conns(newmsg)


def server_connect(address):
    ss = socket.socket()
    ss.bind(address)
    ss.listen(100)
    print('<-------server started-------->')

    while 1:
        try:
            conn, addr = ss.accept()
            connlist.append(conn)
            print('{} connected'.format(addr))

            lock.acquire()
            pools.submit(partial(server_recv, conn, addr))
            lock.release()

        except Exception:
            ss.close()
            print('connection lost')


if __name__ == "__main__":
    address = ('127.0.0.1', 8100)
    server_connect(address)
