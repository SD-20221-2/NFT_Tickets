
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

    #Quebra a mensagem recebida
    nota01, nota02, nota03 = msg.split('-')

    #Transforma de string para Float
    nota01 = float(nota01)
    nota02 = float(nota02)
    nota03 = float(nota03)
    
    #Calcula a média
    media = (nota01+nota02)/2
  
    #Verifica a média do Aluno
    if media >=7:
        mensagem = 'Aluno Aprovado!'

    elif media > 3 and media < 7:
        if (nota03 + media)/2 >= 5:
            mensagem = 'Aluno fez a N3 e foi Aprovado!'

        else: 
            mensagem = 'Aluno fez a N3 e foi Reprovado!'
    
    else :
        mensagem = 'Aluno Reprovado!'
   
   #Envia a mensagem para o cliente
    conexao.send(mensagem.encode())

#Encerra a Conexão
conexao.close()



