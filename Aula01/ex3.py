import random

jogador = input("PEDRA, PAPEL ou TESOURA? ")

lista = ["PEDRA", "PAPEL", "TESOURA"]
computador = random.choice(lista)
print("O computador escolheu: ", computador)

if jogador == computador:
    print("Empatou")

elif jogador == "PEDRA":
    if computador == "PAPEL":
        print ("Computador ganhou")
    if computador == "TESOURA":
        print ("Ganhou but")

elif jogador == "PAPEL":
    if computador == "TESOURA":
        print ("Computador ganhou")
    if computador == "PEDRA":
        print ("Ganhou but")

elif jogador == "TESOURA":
    if computador == "PEDRA":
        print ("Computador ganhou")
    if computador == "PAPEL":
        print ("Ganhou but")

#Maria Eduarda N31
#Kemilly Emanuelly N26