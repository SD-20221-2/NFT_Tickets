import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getMaioridade(self,sexo,idade):
        if sexo.lower() == "masculino":
            if idade >= 18:
                return "A pessoa ja atingiu a maioridade"
        elif sexo.lower() == "feminino":
            if idade >= 21:
                return "A pessoa ja atingiu a maioridade"
        else:
            return 'A pessoa ainda nao atingiu a maioridade'

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Maioridade',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)