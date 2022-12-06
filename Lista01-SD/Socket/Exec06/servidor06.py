
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

    #Quebra a mensagem recebida do Cliente
    nome, nivel, salarioBruto, nDependentes = msg.split('-')

    #Transforma os valores de String para Float
    salarioBruto = float(salarioBruto)
    nDependentes = float(nDependentes)

    #Verifica o Nível
    if nivel.upper() == "A":
        #Verifica o número de dependentes
        if nDependentes > 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.08)

        elif nDependentes == 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.03)

    #Verifica o Nível
    elif nivel.upper() == "B":
        #Verifica o número de dependentes
        if nDependentes > 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.1)

        elif nDependentes == 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.05)

    #Verifica o Nível
    elif nivel.upper() == "C":
        #Verifica o número de dependentes
        if nDependentes > 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.15)

        elif nDependentes == 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.08)
    
    #Verifica o Nível
    elif nivel.upper() == "D":
        #Verifica o número de dependentes
        if nDependentes > 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.17)

        elif nDependentes == 0:
            salarioFinal = salarioBruto - (salarioBruto * 0.1)
    
    #Transforma em String para envio
    salarioFinal = str(salarioFinal)

    #Compacta a mensagem
    mensagem = (nome + '-' + nivel + '-' + salarioFinal)

    #Envia a mensagem para o cliente
    conexao.send(mensagem.encode())

#Encerra a conexão
conexao.close()



