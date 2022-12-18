# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Carta = Pyro4.core.Proxy('PYRO:Carta@' + ipAddressServer + ':9090')

valor = input(" Digite o valor da carta: ")
naipe = input(" Digite o naipe da carta: ")

print(Carta.getCarta(int(valor),int(naipe)))
 