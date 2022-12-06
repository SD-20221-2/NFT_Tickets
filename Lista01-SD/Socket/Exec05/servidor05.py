
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
    idade = conexao.recv(1024).decode()

    if not idade:
        break

    #Transforma a idade para inteiro
    idade = int(idade)

    #Verifica a em qual categoria a pessoa se encaixa
    if idade >= 5 and idade <= 7:
        msg = "Infantil A!"

    elif idade >= 8 and idade <= 10:
        msg = "Infantil B!"

    elif idade >= 11 and idade <= 13:
        msg = "Juvenil A!"

    elif idade >= 14 and idade <= 17:
        msg = "Juvenil B!"
        
    elif idade >= 18:
        msg = "Adulto!"
        
    #Envia a mensagem para o Cliente
    conexao.send(msg.encode())
#Encerra a conexão
conexao.close()



