import socket
import threading

igname=input("choose your NAME peasant: ")

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

def recieve():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='ign':
                client.send(igname.encode('ascii'))
                pass
            else:
                print(message)
        except:
            print('Error bossman')
            client.close()
            break


def write():
    while True:
        message=f'{igname}: {input("")}'
        client.send(message.encode('ascii'))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
                      