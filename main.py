from server import Server
import socket
from app.utils import Logger

log = Logger()

if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    port = 23457
    s.bind((host, port))
    s.listen(5)
    log.info("""
           ___   __________________   _____ __________ _    ____________ 
          /   | / ____/_  __/ ____/  / ___// ____/ __ \ |  / / ____/ __ \\
         / /| |/ /     / / / /_      \__ \/ __/ / /_/ / | / / __/ / /_/ /
        / ___ / /___  / / / __/     ___/ / /___/ _, _/| |/ / /___/ _, _/ 
       /_/  |_\____/ /_/ /_/       /____/_____/_/ |_| |___/_____/_/ |_|  
    """)
    server = Server(socket=s)
