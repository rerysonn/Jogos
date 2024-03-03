print("|--------------------------|")
print("|      Jogo da forca       |")
print("|--------------------------|")

palavra_secreta = "banana"

enforcou = False
acertou = False

while(not acertou and not enforcou):

    chute = input("Qual a letra? ")
    chute = chute.strip()

    
