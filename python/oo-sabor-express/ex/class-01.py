class Livro:
    def __init__(self, titulo='', autor='',paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'
    
    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'
    
    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
        