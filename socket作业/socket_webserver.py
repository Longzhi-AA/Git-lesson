import socket

address = ('0.0.0.0', 18885)

ss = socket.socket()

ss.bind(address)
ss.listen(3)

res = b""

response_header = """
HTTP/1.1 200 OK
"""
response_tab = "\r\n"

response_body = "hello,world"

response = response_header + response_tab + response_body

while 1:
    conn, addr = ss.accept()
    print('{} connected'.format(addr))
    msg = conn.recv(65535)
    res += msg
    print(res.decode())
    ss.send(response.encode())
    print('send over')
    ss.close()