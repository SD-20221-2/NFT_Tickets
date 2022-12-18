# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Cartao = Pyro4.core.Proxy('PYRO:Cartao@' + ipAddressServer + ':9090')

saldo_medio = input("Digite o saldo medio: ")

print(str(Cartao.getCredito(float(saldo_medio))))
 