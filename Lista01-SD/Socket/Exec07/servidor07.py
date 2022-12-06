
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
    #Recebe a mensagem do cliente
    msg = conexao.recv(1024).decode()

    if not msg:
        break

    #Salva as informações nas variáveis
    idade, tempoDeServico= msg.split('-')
 
    #Transforma os valores de String para Inteiros
    tempoDeServico = int(tempoDeServico)
    idade = int(idade)
    
    if idade >=65:
        mensagem = "O Funcionário pode Aposentar!"

    elif tempoDeServico >=30:
        mensagem = "O Funcionário pode Aposentar!"

    elif tempoDeServico >=25 and idade >= 60:
        mensagem = "O Funcionário pode Aposentar!"

    else :
        mensagem = "O Funcionário não pode Aposentar!"

    #Envia a mensagem para o cliente
    conexao.send(mensagem.encode())

#Encerra a conexão
conexao.close()



