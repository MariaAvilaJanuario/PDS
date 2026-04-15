lista=[]
num=input("Digite um número: ")
while (num!=0):
    num=int( input("Digite outro número: "))
    lista.append(num)
    
cont = 0
for L in lista:
    if (L>5):
        cont=cont+1
print("Números maiores que 5: ", L)
   
