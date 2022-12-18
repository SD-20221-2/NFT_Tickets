import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getSalarioLiquido(self,nivel,salario_bruto,nd):
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

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Salario',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)