import socket

address = ('127.0.0.1', 18881)

ss = socket.socket()

ss.bind(address)
ss.listen(3)

res = b""
conn,addr = ss.accept()
print('{} connected'.format(addr))
msg = conn.recv(65535)
res += msg
#
# headers = b"GET / HTTP/1.1\r\nHost: 127.0.0.1:18880\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\n"\
#     b"Upgrade-Insecure-Requests: 1\r\n"\
#     b"\User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.127\r\n"\
#     b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"\
#     b"Accept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n"
# responde = res.decode().split('\r\n\r\n',0)
# req_header = responde[0]
# print(req_header)
# if req_header == headers:

response = b"""HTTP/1.1 200 OK\r\n\r\n
Hello,world!"""

ss.send(response)
print('send over')
ss.close()