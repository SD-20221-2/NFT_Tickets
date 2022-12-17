from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080

def getSituacao(n1,n2,n3):
    m = (n1+n2)/2
  
    if m >=7:
        return "O aluno foi aprovado"
    elif m > 3:
        if (n3 + m)/2 >= 5:
            return "O aluno foi aprovado"
    else :
        return "O aluno foi reprovado"

print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getSituacao,"getSituacao")
servidor.serve_forever()