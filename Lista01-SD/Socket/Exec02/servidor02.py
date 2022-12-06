
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

    #Recebe a mensagem do Cliente
    msg = conexao.recv(1024).decode()
    if not msg:
        break

    #Guarda as informações
    nome, sexo, idade = msg.split('-')

    #Transforma a idade (String) em float
    idade = float(idade)

    #Verifica o sexo
    if sexo.lower() == "masculino":
        #Verifica a idade
        if idade >= 18:
            mensagem = 'Atingiu a maioridade!'
        else:
            mensagem = 'Não atingiu a maioridade!'

    #Verifica o sexo
    elif sexo.lower() == "feminino":
        #Verifica a idade
        if idade >= 21:
            mensagem = 'Atingiu a maioridade!'
        else:
            mensagem = 'Não atingiu a maioridade!'

    #Envia a mensagem para o cliente
    conexao.send(mensagem.encode())

#Encerra a conexão
conexao.close()



