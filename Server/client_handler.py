from socket import socket
from pickle import dumps, loads

def client_handler(client: socket, clients_data):
    client.send(dumps("Hello, World!"))
    client.close()