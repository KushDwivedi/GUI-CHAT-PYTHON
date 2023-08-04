import socket
import threading
HOST='Your IP address'
PORT =8088
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST,PORT))

server.listen()
clients=[]
nicknames=[]
def broadcast(message):
    for client in clients:
        client.send(message)

def handel(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nicknames[client.index(client)]} says {message}")
            broadcast(message)
        except:
            index=client.index(client)
            client.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break


def reciver():
    while True:
        client , address=server.accept()
        print(f"Connected with {str(address)}!..")

        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handel,args=(client,))
        thread.start()

print("---Server Running---")
reciver()
