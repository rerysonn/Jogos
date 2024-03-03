print("|--------------------------|")
print("|      Jogo da forca       |")
print("|--------------------------|")

palavra_secreta = "banana".upper()
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

        
