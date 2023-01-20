
print("Valores de usuario")
num1=int(input('Dame valor 1: '))
num2=int(input('Dame valor 2: '))

if(num1 > num2):
    print("Este {} es mayor que este {}".format(num1,num2))
else:
    print("Este {1} es mayor que este {0}".format(num1,num2))
