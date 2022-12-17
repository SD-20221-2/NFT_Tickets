import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

nome = input(" Digite o nome do funcionario: ")
salario = input(" Digite o salario do funcionario: ")
cargo = input(" Digite o cargo do funcionario: ")

salarioAtualizado = servidor.getSalario(cargo,float(salario))

print('Nome : ' + nome + "\nSalario Ajustado : " + str(salarioAtualizado) + "\n")