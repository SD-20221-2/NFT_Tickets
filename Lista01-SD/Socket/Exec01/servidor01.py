
import socket

#Define a porta padrão para a 8080
porta = 8080

#Método que pega o nome do localhost
host = socket.gethostname()

#Define o Socket
socketServidor = socket.socket()

#Seta a conexão e a porta que irá receber a mensagem
socketServidor.bind((host, porta))

#Faz com que o Socket comece a escutar a porta
socketServidor.listen(1)

#Aceita a conexão
conexao, end = socketServidor.accept()

#Laço para garantir que a mensagem chegará completa
while True:

    #Recebe a mensagem enviada pelo cliente (Tamanho de 1024 bytes)
    msg = conexao.recv(1024).decode()

    if not msg:
        break


    #Quebra a mensagem recebida nos pontos marcados
    mensagem = msg.split('-')

    #Insere cada parte da informação em uma variável
    nome = mensagem[0]
    salario = float(mensagem[1])
    cargo = mensagem[2]

    #Verifica o cargo do funcionário
    if cargo.lower() == "programador":
        #Faz o cálculo do salário do funcionário
        salario = salario * 1.18
    elif cargo.lower() == "operador":
        #Faz o cálculo do salário do funcionário
        salario = salario * 1.2

    #Compacta a mensagem com os símbolos de controle
    msg = (nome + '-' + str(salario) + '-' + cargo) 

    #Envia a resposta para o cliente
    conexao.send(msg.encode())

#Encerra a conexão
conexao.close()



