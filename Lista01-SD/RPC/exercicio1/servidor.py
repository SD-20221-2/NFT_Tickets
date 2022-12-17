from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getSalario(cargo,salario):
    if cargo.lower() == "programador":
        salario = salario * 1.18
        return str(salario)
    elif cargo.lower() == "operador":
        salario = salario * 1.2
        return str(salario)
    else:
        return str(cargo.lower() + ' Não cadastrado')

print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getSalario,"getSalario")
servidor.serve_forever()