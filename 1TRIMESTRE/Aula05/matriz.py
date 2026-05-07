matriz = []

qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

for i in range(qtdLinhas):
    linha = []
    for j in range(qtdColunas):
        linha.append(0)
    matriz.append(linha)

for x in matriz:
    print(x)