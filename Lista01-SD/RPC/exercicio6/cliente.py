import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

nome = input(" Digite o nome: ")
nivel = input(" Digite o nivel: ")
salario_bruto = input(" Digite o salario bruto: ")
nd = input(" Digite o numero de dependentes: ")

print('Nome: ' + nome + '\nNível: ' + nivel + '\nSalario Liquido: ' + str(servidor.getSalarioLiquido(nivel,float(salario_bruto),int(nd))))
