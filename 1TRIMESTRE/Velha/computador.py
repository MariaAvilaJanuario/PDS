import random
tabuleiro = []

def mostraTabuleiro():
    for i in range(3):
        print(tabuleiro[i][0] + " |" + tabuleiro[i][1] + " | " + tabuleiro[i][2])
        if (i!=2):
            print("-"*8)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(" ")
    tabuleiro.append(linha)

jogadas = 0
while(True):
    mostraTabuleiro()


    while(True):
        chuteL = int(input("Jogador X digite a linha ")) -1
        chuteC = int(input("Jogador X digite a coluna ")) -1

        if(tabuleiro[chuteL][chuteC] == " "):
            tabuleiro[chuteL][chuteC] = "X"
            jogadas += 1
            break

        elif (tabuleiro[chuteL][chuteC] == "X"):
            print("Já está preenchido")

        else:
            print("Posição inválida")


    while(True):
        mostraTabuleiro()
        chuteL2 = int(input("Jogador O digite a linha ")) -1
        chuteC2 = int(input("Jogador O digite a linha ")) -1

        if(tabuleiro[chuteL2][chuteC2] == " "):
            tabuleiro[chuteL2][chuteC2] = "O"
            jogadas += 1
            
            break

        elif(tabuleiro[chuteL2][chuteC2] == "X"):
            print("Já está preenchido")


        else:
            print("Posição inválida")

    
    if (jogadas==9):
        break

    