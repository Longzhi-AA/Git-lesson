# server端
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#初始化(AF_INET 网络层IPV4协议（AF_INET6 IPV6)，SOCK_STREAM表示tcp协议， SOCK_DGRAM表示UDP协议）

l_addr = ('127.0.0.1', 41901)
server.bind(l_addr)
# 绑定IP 端口
server.listen()
        # print('service ended')
        # 监听
conn, addr = server.accept()
print('{}:connected'.format(addr))
while 1:
    try:

        msg = conn.recv(1460)
        print('客户端：{}'.format(msg.decode()))
        # mss 报文最大量，tcp默认1460:  最大接受1500， tcp 20， IP20 理论最大值65535-40 =65495
        s_msg = '消息收到'
        conn.send(s_msg.encode())
    except Exception:
        break
server.close()



