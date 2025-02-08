import re

texto = input("Digite o texto a ser revisado: ")
palavra_antiga = input("Qual palavra deseja substituir? ")
palavra_nova = input("Qual a nova palavra? ")

nova_frase = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, texto)
print(nova_frase)