import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getCredito(self,saldo_medio):
        if saldo_medio <=200:
            return 0
        elif saldo_medio >200 and saldo_medio<=400:
            return saldo_medio *0.20
        elif saldo_medio >400 and saldo_medio<=600:
            return saldo_medio *0.30
        elif saldo_medio >600:
            return saldo_medio *0.40

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Cartao',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)