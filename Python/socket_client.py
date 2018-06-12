# Author:YSY

import socket

'''
client = socket.socket()
client.connect(('localhost',6969))

while True:
    msg = input('>>：').strip()
    if len(msg)==0:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
'''

client = socket.socket()
client.connect(('localhost', 8989))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size =client.recv(1024)
    print("发送命令长度:",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size<int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size+=len(data)
        received_data+=data
    else:
        print("cmd执行结果已经接受完毕：",received_size)
        print(received_data.decode())

client.close()