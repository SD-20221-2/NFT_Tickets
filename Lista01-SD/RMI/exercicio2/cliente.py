# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Maioridade = Pyro4.core.Proxy('PYRO:Maioridade@' + ipAddressServer + ':9090')
nome = input(" Digite o nome: ")
sexo = input(" Digite o sexo: ")
idade = input(" Digite a idade: ")
 
print('Nome : ' + nome + '\n' + Maioridade.getMaioridade(sexo,int(idade)))