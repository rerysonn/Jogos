import random

print("|--------------------------|")
print("|      Jogo da forca       |")
print("|--------------------------|\n")
print("Dica do jogo: JOGOS")
print("---------------------\n")


# Trecho de codigo que faz escolher a palavra dentro de um arquivo .txt separado
arquivo = open("D:\\Python projetos\\jogos1\\palavras.txt", "r") # No primeiro parametro, voce deve colocar o caminho do arquivo .txt
palavras = [] # Lista de palavras

#Logica para v
for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha) # Funcao para adicionar strings no final da lista palavras

arquivo.close() # Fechar a conexao entre arquivo e codigo

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()

letras_acertadas = ["_" for letra in palavra_secreta]

# Variaveis que começam com valores Falsos
enforcou = False
acertou = False
erros = 0 # A variavel erros inicializa com 0,

print(letras_acertadas)

# Logica para verificar se acertou ou enforcou
while(not acertou and not enforcou):
    
    # Entrada de dados do usuario
    chute = input("Qual a letra? ")
    chute = chute.strip().upper() #A funcao STRIP retira espaços que possam contar antes ou depois do que foi digitado

    # Verifica se o chute do usuario esta dentro da palavra secreta
    if(chute in palavra_secreta):
        index = 0 # Posição da letra dentro da palavra

        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1

    enforcou = erros == 7 # A variavel que inicializava com valor Falso, agora recebe os erros ate chegar em 7
    acertou = "_" not in letras_acertadas # A Variavel acertou recebe True quando nao existir "_" dentro de letras acertadas
    print(letras_acertadas)

    if(acertou):
        print("------------------")
        print(f"Você GANHOU o jogo!!\nA palavra era: {palavra_secreta}")
    elif(enforcou):
        print("------------------")
        print(f"Você perdeu...\nA palavra era: {palavra_secreta}")

        
