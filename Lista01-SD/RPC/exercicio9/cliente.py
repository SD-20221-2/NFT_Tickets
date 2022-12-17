import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

valor = input(" Digite o valor da carta: ")
naipe = input(" Digite o naipe da carta: ")

print(servidor.getCarta(int(valor),int(naipe)))
