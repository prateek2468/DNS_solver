import socket 
import threading 

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn , addr):
    print(f"[New Connections]{addr} connected . ")
    
    connected= True 
    while connected:
        length = conn.recv(HEADER).decode(FORMAT)
        if length:
            length = int(length)
            msg = conn.recv(length).decode(FORMAT)
            if msg == "fuck off":
                connected = False
            print(f"[{addr}] {msg}")
        
    conn.close()    
        
    

# new connection 
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client , args= (conn , addr) )
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() -1 } ")

print("Server Starting .....")
start()