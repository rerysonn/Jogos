print("|-----------------------------|")
print("|     JOGO DA ADIVINHAÇÃO     |")
print("|-----------------------------|")

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

print(f"Total de jogadas : {total_jogadas}")
