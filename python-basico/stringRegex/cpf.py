import re

cpf = cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")  
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao, cpf):
    print("O CPF está no formato correto")
else:
    print("O CPF está no formato incorreto")