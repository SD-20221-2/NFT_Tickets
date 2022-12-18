# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Peso = Pyro4.core.Proxy('PYRO:Peso@' + ipAddressServer + ':9090')

altura = input("Digite a altura: ")
sexo = input("Digite o sexo: ")

print('Peso Ideal : ' + str(Peso.getPesoIdeal(sexo,float(altura))))
 