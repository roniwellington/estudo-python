class Carro:
    def __init__(self, modelo, cor, anos):
        self.modelo = modelo
        self.cor = cor
        self.anos = anos
meu_carro = Carro(modelo='Fusca', cor='Azul', anos=1970)
print(vars(meu_carro))


class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliação, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliação = nota_avaliação

    def __str__(self):
        return f'{self.nome} | {self.capacidade}'
    
#restaurante_formatado = Restaurante(nome='Bom sabor', categoria='Tradicional')
#print(vars(restaurante_formatado))
restaurante_exemplo = Restaurante(nome='Comida boa', categoria='Gourmet', ativo=True, capacidade=50, nota_avaliação=4.5)

#novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')
print(vars(restaurante_exemplo))
#print(vars(novo_restaurante))


class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')   

print(vars(cliente1))
print(vars(cliente2))
print(vars(cliente3))