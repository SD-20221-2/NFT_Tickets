import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    valor_carta = {
            1: 'As', 2: 'Dois', 3: 'Tres', 4: 'Quatro', 
            5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove',
            10: 'Dez', 11: 'Valete', 12: 'Dama', 13: 'Rei'
            }
    naipe_carta = {
        1: 'Ouros',2:'Pus',3: 'Copas',4: 'Espadas'
        }

    def getCarta(self,valor,naipe):
        return 'A sua carta e: ' + str(self.valor_carta[valor]) + ' de ' + str(self.naipe_carta[naipe])

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Carta',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)