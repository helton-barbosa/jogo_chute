print("******************************************")
print("*******BEM-VINDO AO JOGO DO CHUTE!********")
print("******************************************")

numero_secreto = 81
tentativas = 3

for rodada in range(1, tentativas + 1) :
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))

    if chute < 1 or chute > 100 :
        print("Desculpe... valor inválido! Escolha um valor entre 1 e 100.")
        continue

    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if acertou:
        print("Você ACERTOU!\n")
        break
    else:
        if maior:
            print("Você NÃO ACERTOU! O seu chute foi maior que o número secreto.\n")
        elif menor:
            print("Você NÃO ACERTOU! O seu chute foi menor que o número secreto.\n")

print("Fim do jogo.")
