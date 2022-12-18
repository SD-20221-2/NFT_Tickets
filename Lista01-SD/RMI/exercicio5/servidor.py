import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getCategoria(self,idade):
        if idade >= 5 and idade <= 7:
            return "Infantil A!"
        elif idade >= 8 and idade <= 10:
            return "Infantil B!"
        elif idade >= 11 and idade <= 13:
            return "Juvenil A!"
        elif idade >= 14 and idade <= 17:
            return "Juvenil B!"
        else:
            return "Adulto!"

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Categoria',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)