from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getSalarioLiquido(nivel,salario_bruto,nd):
    if nivel.upper() == "A":
        if nd > 0:
            return salario_bruto - (salario_bruto * 0.08)
        if nd == 0:
            return salario_bruto - (salario_bruto * 0.03)
    if nivel.upper() == "B":
        if nd > 0:
            return salario_bruto - (salario_bruto * 0.1)
        if nd == 0:
            return salario_bruto - (salario_bruto * 0.05)
    if nivel.upper() == "C":
        if nd > 0:
            return salario_bruto - (salario_bruto * 0.15)
        if nd == 0:
            return salario_bruto - (salario_bruto * 0.08)
    if nivel.upper() == "D":
        if nd > 0:
            return salario_bruto - (salario_bruto * 0.17)
        if nd == 0:
            return salario_bruto - (salario_bruto * 0.1)

print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getSalarioLiquido,"getSalarioLiquido")
servidor.serve_forever()