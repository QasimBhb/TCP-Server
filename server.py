import threading 
import socket

host= '127.0.0.1' #localhost
port= 55555

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
ignames=[]

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index[client]
            clients.remove(client)
            client.close()
            igname=ignames[index]
            broadcast(f'{igname} left the chat'.encode('ascii'))
            ignames.remove(igname)
            break


def recieve():
    while True:
        client, address=server.accept()
        print(f"Connected with {str(address)}")


        client.send('NICK'.encode('ascii'))
        igname=client.recv(1024).decode('ascii')
        ignames.append(igname)
        clients.append(client)

        print(f'igname of the client is {igname}')
        broadcast(f'Dude joined with the bussin name of {igname}'.encode('ascii'))
        client.send("enters the room with an attitude".encode('ascii'))

        thread =threading.Thread(target=handle, args=(client,))
        thread.start()

print("i have ears")
recieve()