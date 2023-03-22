import socket
import select
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host, server_port = "localhost", 55555
server_socket.bind((server_host, server_port))
server_socket.listen(4)
print(f"Serveur de chat démarré sur {server_host}:{server_port}")
client_sockets = []

while True:
# Attendre que des clients se connectent ou que des messages soient reçus
	read_sockets, _, _ = select.select([server_socket] + client_sockets, [], [])
	for s in read_sockets:
			if s == server_socket:  # Un nouveau client vient de se connecter
				client_socket, client_address = server_socket.accept()
				client_sockets.append(client_socket)
				"""for client in client_sockets:
					if client != s:
						print(f"Un nouveau client s'est connecté : {client_address}")
						d= {"user":"serveur","message":"Une nouvelle personne s'est connecté !"}
						data = pickle.dump(d)
						client.send(data )"""
					
			else:  # Un message a été reçu
				try:
					message = s.recv(1024)
					if message:
    
						message_dict = pickle.loads(message)
						print(f"Message reçu : {message_dict}")
						#savoir si la clé user est "serveurinfo"
						if message_dict["type"] == "connexion":
							print("serveurinfo")
							#envoyer le message à tous les clients connectés 
							for client in client_sockets:
								client.send(message)

						# Envoyer le message à tous les clients connectés (sauf celui qui l'a envoyé)
						for client in client_sockets:
							if client != s:
								client.send(message)
					else:  # La connexion a été fermée par le client
						print(f"Un client s'est déconnecté : {s.getpeername()}")
						client_sockets.remove(s)
						s.close()
				except ConnectionResetError:  # La connexion a été fermée de manière inattendue
					print(f"Un client a fermé la connexion de manière inattendue : {s.getpeername()}")
					client_sockets.remove(s)
					s.close()			

