import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

altura = input("Digite a altura: ")
sexo = input("Digite o sexo: ")

print('Peso Ideal : ' + str(servidor.getPesoIdeal(sexo,float(altura))))
