import random


def jogar():

    print("***********************")
    print("Bem vindo no jogo de Adivinhação!")
    print("***********************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível acima:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print(numero_secreto)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Número inválido, Digite um número de 1 a 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if (maior):
                print("Você arrou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))

        # rodada = rodada + 1

    print("Fim do Jogo")


if (__name__ == "__main__"):
    jogar()
