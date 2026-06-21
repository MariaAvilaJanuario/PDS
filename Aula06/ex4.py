import random
lista = []
i=0

while(True):
    try:
        tamanho = int(input("Digite qual o tamanho da lista: "))
        corte = int(input("Digite o valor de corte: "))
        if (tamanho<0 or corte<0):
            raise Exception("Não aceitamos números negativos")
        
    except ValueError:
        print("Valor inválido.")
    else:
        break



while(i<tamanho):
    z = random.randrange(tamanho)
    lista.append(z)
    i += 1

contador = 0
i=0
while(i<tamanho):
    if(lista[i]>corte):
        contador+=1
    i += 1

print()
print(f"Existem {contador} números maiores que {corte}")
print(f"A lista era: {lista}")