import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def getSituacao(self,n1,n2,n3):
        m = (n1+n2)/2
    
        if m >=7:
            return "O aluno foi aprovado"
        elif m > 3:
            if (n3 + m)/2 >= 5:
                return "O aluno foi aprovado"
        else :
            return "O aluno foi reprovado"

Pyro4.Daemon.serveSimple({
    GreetingMaker: 'Situacao',
}, host="127.0.0.1", port=9090, ns=False, verbose=True)