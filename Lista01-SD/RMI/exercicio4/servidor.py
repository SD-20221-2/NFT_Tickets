import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getPesoIdeal(self,sexo,altura):
        if sexo.lower() == "masculino":
            return (72.7*altura) - 58
        elif sexo.lower() == "feminino":
            return (62.1*altura) - 44.7

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Peso',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)