# saved as greeting-client.py
import Pyro4

ipAddressServer = "127.0.0.1" # TODO add your server remote IP here

# Works for Python3, see edit above for notes on Python 2.x

Salario = Pyro4.core.Proxy('PYRO:Salario@' + ipAddressServer + ':9090')
nome = input(" Digite o nome do funcionario: ")
salario = input(" Digite o salario do funcionario: ")
cargo = input(" Digite o cargo do funcionario: ")

salarioAtualizado = Salario.getSalario(cargo,float(salario))

print('Nome : ' + nome + "\nSalario Ajustado : " + str(salarioAtualizado) + "\n")