import random

x=random.randrange(101)

chute=input("Digite um valor: ")
chute=int(chute)

while (chute!=x):
    if (chute>x):
        print("Chute muite alto, tente novamente")
    if (chute<x):
        print("Chute muito baixo, tente novamente")
    chute=input("Digite outro valor: ")
    chute=int(chute)
print("Acertou but, +999 de aura")

#Maria Eduarda N31
#Kemilly Emanuelly N26