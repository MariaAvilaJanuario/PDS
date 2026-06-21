import random

tabuleiro = []
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(" ")
    tabuleiro.append(linha)


def mostraTabuleiro():
    for i in range(3):
        print(tabuleiro[i][0] + " |"+tabuleiro[i][1] + " |" + tabuleiro[i][2])
        if (i!=2):
            print("-"*8)


def fazJogada(jogador):
    while(True):
        chuteL = int(input("Digite a Linha:"))-1
        chuteC = int(input("Digite a Coluna:"))-1

        if (tabuleiro[chuteL][chuteC] == " "):
             tabuleiro[chuteL][chuteC] = jogador
             
             return verificaVitoria(chuteL, chuteC, jogador)
        
        print("Jogada Inválida")


def computadorJoga():
    while(True):
        chuteL = random.randrange(3)
        chuteC = random.randrange(3)

        if (tabuleiro[chuteL][chuteC] == " "):
            tabuleiro[chuteL][chuteC] = "O"

            return verificaVitoria(chuteL, chuteC,"O")
        
def verificaVitoria(chuteL, chuteC,jogador):
        cont=0

        #Verifica a Linha
        for i in range(3):
            if (tabuleiro[chuteL][i] == jogador):
                cont +=1
        if(cont == 3):
            print("Vitória de " + jogador)
            return True
        else:
            cont=0

        #Verifica a Coluna
        for i in range(3):
            if (tabuleiro[i][chuteC] == jogador):
                cont +=1
        if(cont == 3):
            print("Vitória de " + jogador)
            return True
        else:
            cont=0

        #Verifica Diagonal \
        for i in range(3):
            if(tabuleiro[i][i] == jogador):
                cont +=1
        if(cont == 3):
            print("Vitória de " + jogador)
            return True
        else:
            cont=0

        #Verifica Diagonal /
        for i in range(3):
            if(tabuleiro[i][2-i] == jogador):
                cont +=1
        if(cont == 3):
            print("Vitória de " + jogador)
            return True
        else:
            cont=0



qtdJogadores = 0
while (qtdJogadores not in [1,2]):
    qtdJogadores = int(input("Quantos jogadores?(1 ou 2):"))
jogadas=0

while(True):
    mostraTabuleiro()
    if(fazJogada("X")):
        break
    jogadas+=1

    if(jogadas == 9):
        print("Empate!")
        break

    if qtdJogadores==2:
        mostraTabuleiro()
        fazJogada("O")
    else:
        computadorJoga()
    jogadas+=1