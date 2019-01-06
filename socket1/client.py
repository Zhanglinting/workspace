import socket


c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

c.connect((host, port))
print('连接成功')
while True:
    msg = input('>>:').strip()
    if len(msg) == 0:
        continue
    if msg == 'exit':
        break
    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))


c.close()
