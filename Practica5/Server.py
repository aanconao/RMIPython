import Pyro4

class PyroServices(object):
    @Pyro4.expose
    def sumar(self, numero1, numero2):
        return numero1 + numero2
    @Pyro4.expose
    def multiplicar(self, numero1, numero2):
        return numero1 * numero2
    @Pyro4.expose
    def dividir(self, numero1, numero2):
        return numero1 / numero2
    @Pyro4.expose
    def restar(self, numero1, numero2):
        return numero1 - numero2

daemon = Pyro4.Daemon()
uri = daemon.register(PyroServices())

print("URI:", uri) #la direccion con nombre de server y su puerto'

daemon.requestLoop()
