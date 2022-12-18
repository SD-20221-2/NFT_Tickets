# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Situacao = Pyro4.core.Proxy('PYRO:Situacao@' + ipAddressServer + ':9090')
n1 = input(" Digite a N1: ")
n2 = input(" Digite a N2: ")
n3 = input(" Digite a N3: ")

print(Situacao.getSituacao(float(n1),float(n2),float(n3)))
 