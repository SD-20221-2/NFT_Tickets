from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getPesoIdeal(sexo,altura):
    if sexo.lower() == "masculino":
        return (72.7*altura) - 58
    elif sexo.lower() == "feminino":
        return (62.1*altura) - 44.7

print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getPesoIdeal,"getPesoIdeal")
servidor.serve_forever()