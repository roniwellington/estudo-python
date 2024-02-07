class Musica:
    def __init__(self, nome = '', artista= '', duracao= 0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

print(vars(musica1))
print(vars(musica2))
print(vars(musica3))

#print(vars(musica1))