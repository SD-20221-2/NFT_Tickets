import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

idade = input("Informe a idade da pessoa: ")

print('A categoria em que a pessoa se enquadra é ' + str(servidor.getCategoria(int(idade))))
