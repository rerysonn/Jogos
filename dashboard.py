import adivinhacao
import forca

def escolha_jogo():
    print("|-------------------------|")
    print("|     Escolha o jogo      |")
    print("|-------------------------|\n")

    print("1 - Adivinhação\n2 - Forca\n")
    escolha = int(input("Escolha:  "))

    if(escolha == 1):
        adivinhacao.jogar()
    elif(escolha == 2):
        forca.jogar()


if(__name__ == "__main__"):
    escolha_jogo()