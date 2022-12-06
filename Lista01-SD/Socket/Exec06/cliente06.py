
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
nome = input("Informe o nome do funcionário: ")
nivel = input("Informe o nível do funcionário: ")
salarioBruto = input("Informe o salário bruto do funcionário: ")
nDependentes = input("Informe o número de dependentes do funcionário: ")

#Compacta a mensagem
msg = (nome + '-' + nivel + '-' + salarioBruto + '-' + nDependentes)

#Envia a mensagem para o servidor
socketCliente.send(msg.encode())

#Recebe a mensagem enviada pelo servidor (Tamanho de 1024 bytes)
mensagem = socketCliente.recv(1024).decode()

#Quebra a mensagem recebida pelo servidor
nome, nivel, salarioLiquido= mensagem.split('-')

#Apresenta as informações
print('O Funcionário ', nome, " possui nível ", nivel, " com salário líquido de R$ ", salarioLiquido)

#Encerra a conexão
socketCliente.close()

