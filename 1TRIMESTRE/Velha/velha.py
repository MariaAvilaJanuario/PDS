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

    chuteL = int(input("Digite a linha ")) -1
    chuteC = int(input("Digite a coluna ")) -1

    if(tabuleiro[chuteL][chuteC] == " "):
        tabuleiro[chuteL][chuteC] = "X"
        jogadas += 1
    else:
        print("Posição inválida")
        continue
    if (jogadas==9):
        break