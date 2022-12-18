# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Aposentadoria = Pyro4.core.Proxy('PYRO:Aposentadoria@' + ipAddressServer + ':9090')

idade = input("Digite a idade: ")
tempo = input("Digite o tempo de servico: ")

print(str(Aposentadoria.getAposentadoria(int(idade),float(tempo))))
 