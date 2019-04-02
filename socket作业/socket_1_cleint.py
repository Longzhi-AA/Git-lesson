import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

l_addr = ('127.0.0.1', 41901)

client.connect(l_addr)
while 1:
    try:
        msg = input('please input:')
        client.send(msg.encode())

        msg = client.recv(1460)
        print('服务端：{}'.format(msg.decode()))
    except Exception:
        break
client.close()