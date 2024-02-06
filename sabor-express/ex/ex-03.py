numero_digitado = int(input('Digite um numero: '))

if numero_digitado % 2 == 0:
    print('numero par')
else:
    print('numero impar')


idade_digitada = int(input('Digite sua idade?'))
if 0 <idade_digitada  <= 12:
    print('é Criança')
elif 12 < idade_digitada <= 18:
    print('Adolescente')
elif idade_digitada > 18:
    print('Adulto')
else:
    print('Valor inválido')

nome = 'julia'
senha = '123'

nome_usuario = input('Digite seu nome de usuario: \n')
senha_usuario = input('Digite sua senha: ')

if nome == nome_usuario and senha == senha_usuario:
    print(f'Bem vindo {nome}')
else:
    print('Acesso negado')


solicitacao_de_coordenadas_x = float(input('Digite a coordenada X : '))
solicitacao_de_coordenadas_y = float(input('Digite a coordenada Y : '))

if solicitacao_de_coordenadas_x > 0 and solicitacao_de_coordenadas_y > 0:
    print('primeiro quadrante')
elif solicitacao_de_coordenadas_x < 0 and solicitacao_de_coordenadas_y > 0:
    print('Segundo quadrante')
elif solicitacao_de_coordenadas_x < 0 and solicitacao_de_coordenadas_y < 0:
    print('Terceiro quadrante')
elif solicitacao_de_coordenadas_x > 0 and solicitacao_de_coordenadas_y < 0:
    print('Quarto quadrante')
else:
    print('Ponto de origem')








