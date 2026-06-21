qtd = int(input("Digite a quantidade de alunos: "))
medias = []
total = 0

while(True):
    try:
        for i in range(qtd):
            print("********************")
            print(f"Notas do {i + 1}° aluno")
            nota1 = float(input(f"1º Nota: "))
            nota2 = float(input(f"2º Nota: "))
            if (nota1<0 or nota2<0):
                raise Exception("O sistema escolar não aceita notas negativas")

            medias.append((nota1 + nota2) / 2)
            
    except ValueError:
        print("Valor inválido.")
    else:
        break

print()
print(f"Médias dos alunos: {medias}")

for i in medias:
    total += i

mediaTotal = total / len(medias)
print(f"Média geral da turma: {mediaTotal}")