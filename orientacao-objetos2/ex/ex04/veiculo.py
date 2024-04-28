# 1) Crie uma classe chamada Veiculo com um método abstrato chamado ligar
# 2) No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
        
    @abstractmethod
    def ligar(self):
        pass
    

# 3) Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4) No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        
    def ligar(self):
        print(f"O carro {self.modelo} está ligador")
            
# 5) Em um arquivo chamado main.py, importe a classe Carro.