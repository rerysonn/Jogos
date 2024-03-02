import random

print("|-----------------------------|")
print("|     JOGO DA ADIVINHAÇÃO     |")
print("|-----------------------------|")


numero_secreto = random.randrange(1,51)
total_jogadas = 0

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
    if(chute < 0 or chute > 100):
        print("Digite um numero que seja valido")
        continue 

    print(f"Você digitou {chute}")


