print("***********************")
print("Bem vindo no jogo de Adivinhação!")
print("***********************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")
print("Você digitou ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você arrou")
