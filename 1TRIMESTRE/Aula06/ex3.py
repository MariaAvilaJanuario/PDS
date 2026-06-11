qtd = int(input("Digite a quantidade de alunos: "))
medias = []


for i in range(qtd):
    print("********************")
    print(f"Notas do {i + 1}° aluno")
    nota1 = float(input(f"1º Nota: "))
    nota2 = float(input(f"2º Nota: "))
    medias.append((nota1 + nota2) / 2)
    print()
print(medias)

for i in medias:
    total =+ 1

mediaTotal = total / medias
print(mediaTotal)