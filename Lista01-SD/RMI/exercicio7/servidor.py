import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getAposentadoria(self,idade,tempo):
        if idade >=65:
            return "O funcionario pode se aposentar"
        elif tempo >=30:
            return "O funcionario pode se aposentar"
        elif tempo >=25 and idade >= 60:
            return "O funcionario pode se aposentar"
        else :
            return "O funcionario não pode se aposentar"

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Aposentadoria',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)