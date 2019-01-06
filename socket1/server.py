import socket


server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server.bind((host,port))
#设置最大连接数,超过后排对
server.listen(5)
# 建立客户端连接
print('等待连接……')
clientskt, addr = server.accept()
print('连接地址:{}'.format(addr))
while True:
        m = clientskt.recv(1024)
        if not m:
            print('没有数据')
            break
        print(m.decode('utf-8'))
        msg = input(">>:").strip()
        if len(msg) == 0:
            continue
        clientskt.send(msg.encode('utf-8'))
clientskt.close()
