from app.utils import Logger
from socket import socket as Socket
from package import receive_package, Header
from threading import Thread

log = Logger()


class Server:
    def __init__(self, socket: Socket):
        self.socket = socket
        self.start_receive_thread()

    def start_receive_thread(self):
        def temp():
            while True:
                sock, addr = self.socket.accept()
                try:
                    result = receive_package(sock)
                    if isinstance(result, Header):
                        header = result
                        log.debug(f"<- message: \"{header.get_message()}\" "
                                  f"| hash: {header.get_package_hashcode()}")
                    else:
                        package = result
                        header = result.get_header()
                        log.debug(f" -> " + package.get_desc())
                except (ConnectionAbortedError, ConnectionResetError):
                    break

        t = Thread(target=temp)
        t.start()
        t.join()
