# Author:YSY

import socket
import os

'''
server = socket.socket()
server.bind(('localhost',6969))
server.listen()
while True:
    conn, addr = server.accept()

    while True:
        data = conn.recv(1024)
        res = os.popen(str(data,encoding='utf-8')).read()
        conn.send(res.encode('utf-8'))

server.close()
'''

server = socket.socket()
server.bind(('localhost',8989))
server.listen()

while True:
    conn,addr = server.accept()
    print("新连接：",addr)
    while True:
        print("正在等待新指令:")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行新指令:",data.decode())
        cmd_res = os.popen(data.decode()).read()
        print(cmd_res)
        if len(cmd_res)==0:
            cmd_res="cmd命令没有输出结果"
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        conn.send(cmd_res.encode('utf-8'))
        print("发送完毕！")

server.close()