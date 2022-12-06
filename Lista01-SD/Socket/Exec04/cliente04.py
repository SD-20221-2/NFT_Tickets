
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
altura = input("Informe a altura da pessoa: ")
sexo = input("Informe o sexo da pessoa: ")

#Compacta a mensagem
msg = (altura + '-' + sexo)

#Envia a mensagem para o servidor
socketCliente.send(msg.encode())

#Recebe a mensagem enviada pelo servidor (Tamanho de 1024 bytes)
mensagem = socketCliente.recv(1024).decode()

#Transforma a mensagem de string para float
mensagem = float(mensagem)

#Apresenta as informações formatando a variável de peso
print("O pesoa ideal dessa pessoa é {:.2f} " .format(mensagem))

#Encerra a conexão
socketCliente.close()

