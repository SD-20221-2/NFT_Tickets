
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
idade = input("Informe a idade da pessoa: ")

#Envia a mensagem para o Serivdor
socketCliente.send(idade.encode())

#Recebe a mensagem enviada pelo servidor (Tamanho de 1024 bytes)
msg = socketCliente.recv(1024).decode()

print("A categoria em que a pessoa se enquadra é ", msg)

#Encerra a Conexão
socketCliente.close()

