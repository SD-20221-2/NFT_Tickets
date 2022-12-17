from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getMaioridade(sexo,idade):
    if sexo.lower() == "masculino":
        if idade >= 18:
            return "A pessoa ja atingiu a maioridade"
    elif sexo.lower() == "feminino":
        if idade >= 21:
            return "A pessoa ja atingiu a maioridade"
    else:
        return 'A pessoa ainda nao atingiu a maioridade'

print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getMaioridade,"getMaioridade")
servidor.serve_forever()