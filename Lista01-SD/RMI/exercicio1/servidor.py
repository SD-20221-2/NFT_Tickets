import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getSalario(self, cargo, salario):
        if cargo.lower() == "programador":
            salario = salario * 1.18
            return str(salario)
        elif cargo.lower() == "operador":
            salario = salario * 1.2
            return str(salario)
        else:
            return str(cargo.lower() + ' Não cadastrado')

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Salario',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)