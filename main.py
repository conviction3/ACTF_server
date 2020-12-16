import socket  # 导入 socket 模块
from app.utils import *

client_num = 2

if __name__ == '__main__':
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = 12345  # 设置端口
    s.bind((host, port))  # 绑定端口

    s.listen(5)  # 等待客户端连接
    print("waiting for client")

    client_count = 0
    data_list = []

    while True:
        c, addr = s.accept()  # 建立客户端连接
        data = c.recv(1024)
        print("客户端{}的计算结果为{}".format(addr, data))
        data_list.append(bytes2int(data))

        c.send(bytes('OK', encoding='utf-8'))
        c.close()  # 关闭连接

        client_count += 1
        if client_count == client_num:
            print("所有客户端均处理完成")
            break

    sum = sum(data_list)
    print("最终计算结果：{}".format(sum))
