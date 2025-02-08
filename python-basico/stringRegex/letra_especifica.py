import re

texto = input("Digite o título dos livro: ") 
letra = input("Digite a letra inicial para pesquisa: ")  
palavras = re.findall(rf'\b{letra}[a-zà-ÿ]*', texto, re.IGNORECASE)
print(palavras)