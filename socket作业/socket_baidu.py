import socket
import os

ss = socket.socket()

addr = ('180.97.33.107', 80)

ss.connect(addr)
headers = b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: closed\r\n" \
          b"ache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\n" \
          b"\User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.127\r\n" \
          b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n\r\n"

ss.send(headers)
res = b""

msg = ss.recv(65535)
print('received')

res += msg
responde = res.decode().split('\r\n\r\n', 1)
html = responde[1]
print(html)

mydir = os.path.dirname(__file__)
filename = os.path.join(mydir, 'baidu.html')
with open(filename, 'w') as f:
    f.write(html)
