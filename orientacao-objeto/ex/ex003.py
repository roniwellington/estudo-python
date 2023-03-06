class Jogo:
    def __init__(self):
        self.contador = 0

    def incrementa(self):
        self.contador += 1

jogo = Jogo()
jogo.incrementa()
print(jogo.contador)
