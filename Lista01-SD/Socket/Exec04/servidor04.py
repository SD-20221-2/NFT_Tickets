
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

    #Quebra a mensagem do Cliente
    altura, sexo = msg.split('-')

    #Transforma a altura para Float já que a mensagem chega como String
    altura = float(altura)

    #Verifica o Sexo da Pessoa
    if sexo.lower() == "feminino":
        #Cálculo do peso ideal
        pesoIdeal = (62.1*altura) - 44.7
    #Verifica o Sexo da Pessoa
    elif sexo.lower() == "masculino":
        #Cálculo do peso ideal
        pesoIdeal = (72.7*altura) - 58
        
    #Transforma o peso para String para que a mensagem possa ser enviada
    pesoIdeal = str(pesoIdeal)
    #Envia a mensagen para o cliente
    conexao.send(pesoIdeal.encode())

#Encerra a conexão
conexao.close()



