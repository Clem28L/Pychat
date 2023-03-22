import socket 
import pickle

# Créer un dictionnaire à envoyer
d = {'key1': 'value1', 'key2': 'value2'}
data = pickle.dumps(d)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 9001
client_socket.connect((host, port))
nom = input("Quelle est votre nom ? ")

while True:

	message = input(f"{nom} > ")
	client_socket.send(data)