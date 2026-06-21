Palavra = input("Digite algo: ")
Palavra = str(Palavra)
print("A quantidade de caracteres é: ",(len(Palavra)))

cont = 0
for L in Palavra:
    if L=="a":
        cont=cont+1
print("A quantidade de letras A é: ",cont)