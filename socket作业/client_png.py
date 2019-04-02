import socket
import os

sc = socket.socket()


address = ('127.0.0.1', 18001)
sc.connect(address)

mydir = os.path.dirname(__file__)
b_file = b""

filename = input('please input filename:')
my_jpg = os.path.join(mydir, filename)
with open(my_jpg, 'rb') as f:
    datas = f.read()
    b_file += datas
    # print(datas)
    sc.send(b_file)
    f.close()
    print('上传成功')

sc.close()