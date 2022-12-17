from xmlrpc.server import SimpleXMLRPCServer

print('\tServidor')

IP = '127.0.0.1'
PORTA = 8080
valor_carta = {
        1: 'As', 2: 'Dois', 3: 'Tres', 4: 'Quatro', 
        5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove',
        10: 'Dez', 11: 'Valete', 12: 'Dama', 13: 'Rei'
        }
naipe_carta = {
    1: 'Ouros',2:'Pus',3: 'Copas',4: 'Espadas'
    }

def getCarta(valor,naipe):
   return 'A sua carta e: ' + str(valor_carta[valor]) + ' de ' + str(naipe_carta[naipe])


print('\n Esperando por clientes')
servidor = SimpleXMLRPCServer((IP,PORTA),allow_none=True)
servidor.register_function(getCarta,"getCarta")
servidor.serve_forever()