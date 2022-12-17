import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

saldo_medio = input("Digite o saldo medio: ")

print(str(servidor.getCredito(float(saldo_medio))))
