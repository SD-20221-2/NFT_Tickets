# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Salario = Pyro4.core.Proxy('PYRO:Salario@' + ipAddressServer + ':9090')

nome = input(" Digite o nome: ")
nivel = input(" Digite o nivel: ")
salario_bruto = input(" Digite o salario bruto: ")
nd = input(" Digite o numero de dependentes: ")

print('Nome: ' + nome + '\nNível: ' + nivel + '\nSalario Liquido: ' + str(Salario.getSalarioLiquido(nivel,float(salario_bruto),int(nd))))
 