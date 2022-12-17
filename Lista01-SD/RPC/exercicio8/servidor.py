from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getCredito(saldo_medio):
    if saldo_medio <=200:
        return 0
    elif saldo_medio >200 and saldo_medio<=400:
        return saldo_medio *0.20
    elif saldo_medio >400 and saldo_medio<=600:
        return saldo_medio *0.30
    elif saldo_medio >600:
        return saldo_medio *0.40


print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getCredito,"getCredito")
servidor.serve_forever()