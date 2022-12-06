
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
idade = input("Informe a idade do funcionário: ")
tempoDeServico = input("Informe o tempo de serviço do funcionário: ")

#Controle para a quebra da mensagem pelo Servidor
mensagem = (idade + '-' + tempoDeServico)

#Envia as mensagens para o Servidor
socketCliente.send(mensagem.encode())

#Recebe a mensagem enviada pelo servidor (Tamanho de 1024 bytes)
msg = socketCliente.recv(1024).decode()

#Mostra a mensagem recebida
print(msg)

#Encerra a conexão
socketCliente.close()

