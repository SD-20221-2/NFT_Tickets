
import socket

#Define a porta padrão para a 8080
porta = 8080

#Método que pega o nome do localhost
host = socket.gethostname()

#Define o Socket
socketCliente = socket.socket()

#Conecta o Socket criado com a porta
socketCliente.connect((host, porta))

#Recebe os inputs do usuário
nomeF = input("Informe o nome do funcionário: ")
salarioF = input("Informe o salário do funcionario: ")
cargoF = input("Informe o cargo do funcionario: ")

#Variável de controle para poder transmitir a mensagem
msg = (nomeF + '-' + salarioF + '-' + cargoF)

#Envia a mensagem para o Servidor
socketCliente.send(msg.encode())

#Recebe a mensagem enviada pelo servidor
msg = socketCliente.recv(1024).decode()

#Quebra mensagem enviada pelo servidor
array = msg.split('-')

print(array)

#Apresenta as informações na tela
print('O nome do funcionário é: ', array[0], 'e possui um salário de : R$' ,array[1])

#Encerra a conexão
socketCliente.close()

