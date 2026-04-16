import random 

valores = []

while (len(valores)<6):
    x=random.randrange(1,61)
    if x not in valores:
        valores.append(x)

print("Os números da mega-sena são: ", valores)

#Maria Eduarda N31
#Kemilly Emanuelly N26