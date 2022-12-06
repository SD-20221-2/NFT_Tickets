
import socket

#Define a porta padrão para a 8080
porta = 8080

#Método que pega o nome do localhost
host = socket.gethostname()

#Define o Socket
socketCliente = socket.socket()

#Conecta o Socket criado com a porta
socketCliente.connect((host, porta))

#Recebe os inputs
valorCarta = input("Informe o valor da carta: ")

naipeCarta = input("Informe o Naipe da carta: ")

#Condensa a mensagem
msg = valorCarta + '-' + naipeCarta

#Envia a mensagem para o Servidor
socketCliente.send(msg.encode())

#Recebe a mensagem do Servidor
mensagem = socketCliente.recv(1024).decode()

#Apresenta a mensagem
print(mensagem)

#Encerra a conexão
socketCliente.close()
