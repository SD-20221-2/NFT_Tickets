
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
nome = input("Informe o nome da pessoa: ")
sexo = input("Informe o sexo da pessoa: ")
idade = input("Informe a idade da pessoa: ")


#Compacta a mensagem
mensagem = (nome + '-' + sexo + '-' + idade)

#Envia a mensagem para o servidor
socketCliente.send(mensagem.encode())

#Recebe a mensagem enviada pelo cliente (Tamanho de 1024 bytes)
mensagem = socketCliente.recv(1024).decode()

#Mostra a mensagem
print(mensagem)

#Encerra a conexão
socketCliente.close()

