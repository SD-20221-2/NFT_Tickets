
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
    #Recebe a mensagem enviada pelo cliente
    saldoMedio = conexao.recv(1024).decode()

    if not saldoMedio:
        break

    #Transforma o saldo para float para que possam ser feitas as comparações e contas
    saldoMedio = float(saldoMedio)

    #Verifica o saldo
    if saldoMedio >= 0 and saldoMedio <= 200:
        #Calcula o Crédito
        valorCredito = 0

    elif saldoMedio >= 201 and saldoMedio <= 400:
        #Calcula o Crédito
        valorCredito = saldoMedio * 0.20

    elif saldoMedio >= 401 and saldoMedio <= 600:
        #Calcula o Crédito
        valorCredito = saldoMedio * 0.30

    elif saldoMedio >= 601:
        #Calcula o Crédito
        valorCredito = saldoMedio * 0.40

    #Transforma os valores para String para que possam ser enviados
    saldoMedio= str(saldoMedio)
    valorCredito = str(valorCredito)
    mensagem = (saldoMedio + '-' + valorCredito)

    #Envia os dados para o cliente
    conexao.send(mensagem.encode())

#Encerra a conexão
conexao.close()



