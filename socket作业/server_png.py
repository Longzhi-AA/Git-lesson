import socket
import os

ss = socket.socket()
address = ('127.0.0.1', 18001)
ss.bind(address)
ss.listen(3)
print('waiting........ ')
mydir = os.path.dirname(__file__)
b_file = b""
conn, addr = ss.accept()
print('{} connected'.format(addr))
data = conn.recv(65535)
b_file += data
file_name = os.path.join(mydir, 'a.jpg')
with open(file_name, 'wb') as f:
    f.write(b_file)
    f.close()
    print('上传成功')
ss.close()

