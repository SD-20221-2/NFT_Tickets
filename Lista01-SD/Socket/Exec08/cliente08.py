
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
saldoMedio = input("Informe o Saldo Médio do Cliente: ")

#Envia a mensagem para o Servidor
socketCliente.send(saldoMedio.encode())

#Recebe a mensagem do Servidor
mensagem = socketCliente.recv(1024).decode()

#Quebra a mensagem recebida
saldoMedio, credito = mensagem.split("-")

#Transforma o valor do crédito de String para flot
credito = float(credito)
print("O Saldo Médio do Cliente é ", saldoMedio, " e o Valor do crédito é de R$ {:.2f}".format(credito))

#Encerra a Conexão
socketCliente.close()

