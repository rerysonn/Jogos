import random

def jogar():
    print("|-----------------------------|")
    print("|     JOGO DA ADIVINHAÇÃO     |")
    print("|-----------------------------|")


    numero_secreto = random.randrange(1,51)
    total_jogadas = 0
    pontos = 1000

    # ESCOLHA DO NIVEL DESEJADO PARA JOGAR
    print("Escolha o nivel que deseja jogar:\n 1 - Fácil\n 2 - Médio\n 3 - Difícil")
    nivel = int(input("Digite o nivel: "))
    print("-------------------------------")

    if(nivel == 1):
        total_jogadas = 15
    if(nivel == 2):
        total_jogadas = 10
    if(nivel == 3):
        total_jogadas = 5


    for rodada in range(1, total_jogadas + 1):
        print(f"Tentativas {rodada} de {total_jogadas}")
        chute = int(input("Digite um numero de 1 a 100: ")) # Entrada de dados do usuario.

        # Caso o usuario coloque um numero fora dos permitidos
        if(chute < 1 or chute > 100):
            print("Digite um numero que seja valido")
            continue 

        print(f"Você digitou: {chute}")

        acertou = numero_secreto == chute # Caso o usuario acerte o numero secreto com seu chute, o valor deve ser armazenezado na variavel acertou
        chute_menor = numero_secreto > chute # Caso o chute seja menor que o numero secreto, sera armazenado na variavel chute_menor
        chute_maior = numero_secreto < chute # Caso o chute seja maior que o numero secreto, sera armazenado na variavel chute_maior
        
        if(acertou):
            print("--------------------------------")
            print(f"Você ACERTOU o numero secreto!!\nSua pontuação foi de {pontos}")
            print("--------------------------------")
            break
        else:
            if(chute_menor):
                print("Seu chute foi MENOR que o numero secreto.")
            elif(chute_maior):
                print("Seu chute foi MAIOR que o numero secreto.")
            
        pontuacao_perdida = abs(numero_secreto - chute)
        pontos -= pontuacao_perdida

if(__name__ == "__main__"):
    jogar()

