import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

nome = input(" Digite o nome: ")
sexo = input(" Digite o sexo: ")
idade = input(" Digite a idade: ")

print('Nome : ' + nome + '\n' + servidor.getMaioridade(sexo,int(idade)))
