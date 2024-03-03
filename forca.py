import random

def jogar():

    abertura_jogo() 
    palavra_secreta = carrega_palavra_secreta() 

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # Quantidade de letras que contem na palavra
    print(letras_acertadas)
    
    # Variaveis
    enforcou = False
    acertou = False
    erros = 0 

    # Logica para verificar se acertou ou enforcou
    while(not acertou and not enforcou):
        
        chute = pede_chute() # Entrada de dados do usuario

        # Verifica se o chute do usuario esta dentro da palavra secreta
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            forca(erros)

        enforcou = erros == 7 # A variavel que inicializava com valor Falso, agora recebe os erros ate chegar em 7
        acertou = "_" not in letras_acertadas # A Variavel acertou recebe True quando nao existir "_" dentro de letras acertadas

        print(letras_acertadas)

        #MENSAGEM DE VENCEDOR OU PERDEDOR
        if(acertou):
            ganhou_jogo()
        elif(enforcou):
            perdeu_jogo()
        
# FUNCOES DO JOGO
# Abertura do jogo
def abertura_jogo(): 
    print("|--------------------------|")   
    print("|      Jogo da forca       |")
    print("|--------------------------|\n")
    print("Dica do jogo: JOGOS")
    print("---------------------\n")

# Palavra secreta que foi selecionada randomicamente 
def carrega_palavra_secreta():
    # No primeiro parametro, deve-se colocar o caminho do arquivo .txt 
    arquivo = open("D:\\Python projetos\\jogos1\\palavras.txt", "r") 
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha) # Funcao para adicionar strings no final da lista palavras

    arquivo.close() # Fechar a conexao entre arquivo e codigo

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavras):
    return["_" for letra in palavras]

def pede_chute():
    # Entrada de dados do usuario
    chute = input("Qual a letra? ")
    chute = chute.strip().upper() #A funcao STRIP retira espaços que possam existir antes ou depois do que foi digitado.
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0 # Posição da letra dentro da palavra

    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

# MENSAGENS DO JOGO
def ganhou_jogo():
    print("------------------")
    print("Parabens!! Você GANHOU!!")

def perdeu_jogo():
    print("------------------")
    print("Você foi enforcado...")

def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()

        
