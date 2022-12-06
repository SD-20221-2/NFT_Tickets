
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
nota01 = input("Informe a Nota 01: ")
nota02 = input("Informe a Nota 02: ")
nota03 = input("Informe a Nota 03: ")

#Soma o valor das notas
notaFinal = (nota01 + '-' + nota02 + '-' + nota03)

#Envia a mensagem para o Servidor
socketCliente.send(notaFinal.encode())

#Recebe a mensagem enviada pelo servidor (Tamanho de 1024 bytes)
mensagem = socketCliente.recv(1024).decode()

print(mensagem)

socketCliente.close()

