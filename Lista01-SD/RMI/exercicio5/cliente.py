# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Categoria = Pyro4.core.Proxy('PYRO:Categoria@' + ipAddressServer + ':9090')

idade = input("Informe a idade da pessoa: ")

print('A categoria em que a pessoa se enquadra é ' + str(Categoria.getCategoria(int(idade))))
 