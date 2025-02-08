import re

texto = input("Digite a descrição da receita: ")
numero = re.findall(r'\d+', texto)[0]
print(f"O número da receita é: {numero}")