from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getAposentadoria(idade,tempo):
    if idade >=65:
        return "O funcionario pode se aposentar"
    elif tempo >=30:
        return "O funcionario pode se aposentar"
    elif tempo >=25 and idade >= 60:
        return "O funcionario pode se aposentar"
    else :
        return "O funcionario não pode se aposentar"


print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getAposentadoria,"getAposentadoria")
servidor.serve_forever()