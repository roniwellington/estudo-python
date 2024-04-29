pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}
print(pessoa)

#Atualização de Idade
pessoa['idade'] = 31

#Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

#Remoção de Elemento
del pessoa['cidade']
print(pessoa)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
