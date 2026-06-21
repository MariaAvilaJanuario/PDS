num1 = input("Digite um número: ");
num1 = int(num1)

num2 = input("Digite outro número: ");
num2 = int(num2)

num3 = input("Digite outro número: ")
num3 = int(num3)

if (num1 > num2):
    if(num1 >  num3):
        print ("O maior número é: " , num1)

if (num2 > num1):
    if (num2 > num3):
        print ("O maior número é: " , num2)

if (num3 > num1):
    if (num3 > num2):
        print ("O maior número é: " , num3)



if (num1 < num2):
    if(num1 <  num3):
        print ("O menor número é: " , num1)

if (num2 < num1):
    if (num2 < num3):
        print ("O menor número é: " , num2)

if (num3 < num1):
    if (num3 < num2):
        print ("O menor número é: " , num3)



média = ((num1 + num2 + num3) / 3);
print ("A média é: " , média);