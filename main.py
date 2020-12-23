import socket
from app.utils import *

node_num = 1

if __name__ == '__main__':
    # create socket instance
    s = socket.socket()
    # local host name
    host = socket.gethostname()
    # set local port
    port = 12345
    # bind local port to local host
    s.bind((host, port))

    s.listen(5)
    print("waiting for connect...")

    client_count = 0
    data_list = []

    while True:
        # establish connect to the client
        c, addr = s.accept()
        data = c.recv(1024)
        print("The calculation result of node {} is {}".format(addr, data))
        data_list.append(bytes2int(data))

        c.send(bytes('OK', encoding='utf-8'))
        # close socket
        c.close()

        client_count += 1
        if client_count == node_num:
            print("All the nodes process done")
            break

    sum = sum(data_list)
    print("Final result is: {}".format(sum))
