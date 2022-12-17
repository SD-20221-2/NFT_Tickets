import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

n1 = input(" Digite a N1: ")
n2 = input(" Digite a N2: ")
n3 = input(" Digite a N3: ")

print(servidor.getSituacao(float(n1),float(n2),float(n3)))
