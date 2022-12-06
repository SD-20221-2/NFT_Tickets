
import socket

#Define a porta padrão para a 8080
porta = 8080

#Método que pega o nome do localhost
host = socket.gethostname()

#Define a Classe Carta
class Carta:

    #Construtor da Classe Carta
    def __init__(self, valorCarta, naipeCarta):
        self.valorCarta = valorCarta
        self.naipeCarta = naipeCarta
    
    #Define a propriedade Nome da Carta
    def nome(self):
        #Define os naipes
        naipe = {1: 'Copas',2:'Paus',3: 'Ouros',4: 'Paus'}

        #Define os Valores
        valor = {1: 'Ás', 2: 'Dois', 3: 'Três', 4: 'Quatro', 5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove', 10: 'Dez', 11: 'Valete', 12: 'Dama', 13: 'Rei'}
        
        #Forma o nome da carta
        nomeCarta = 'A carta informada é ' + valor[self.valorCarta] + ' de ' + naipe[self.naipeCarta] + ' !'
        return (nomeCarta)

#Define o Socket - AF_INET -> IPV4; SOCK_STREAM -> TCP
socketServidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Seta a conexão e a porta que irá receber a mensagem
socketServidor.bind((host, porta))

#Faz com que o Socket comece a escutar a porta
socketServidor.listen(3)

#Aceita a conexão
conexao, end = socketServidor.accept()

#Laço para garantir que a mensagem chegará completa
while True:

        #Recebe a mensagem do Cliente
        msg = conexao.recv(1024).decode()

        if not msg:
            break

        #Quebra a mensagem do Cliente
        valorCarta, naipeCarta = msg.split('-')

        #Transforma os valores para inteiros
        valorCarta = int(valorCarta)
        naipeCarta = int(naipeCarta)
        
        #Instancia a carta como um Objeto de Carta
        carta = Carta(valorCarta, naipeCarta)

        #Pega o nome da carta
        mensagem = carta.nome()

        #Envia a mensagem para o Cliente
        conexao.send(mensagem.encode())

#Encerra a conexão
conexao.close()
