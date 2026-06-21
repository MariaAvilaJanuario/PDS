lista = [1, 4, 5, 7, 8, 100]

while(True):
    try:
        x = int(input("Digite o índice: "))
        print(f"O elemento do índice {x} é {lista[x]}")
        if (x<0):
            raise Exception("Não aceitamos números negativos")
        
    except ValueError:
        print("Valor inválido.")
        
    except IndexError:
        print("Esse índice não existe em nossa lista")

    else:
        break