import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://127.0.0.1:8080")

idade = input("Digite a idade: ")
tempo = input("Digite o tempo de servico: ")

print(str(servidor.getAposentadoria(int(idade),float(tempo))))
