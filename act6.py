#Calcula el mayor de tres números introducidos

num1 = int(input("introduce tu primer numero: "))
num2 = int(input("introduce tu segundo numero: "))
num3 = int(input("introduce tu tercer numero: "))

if num1 > num2 and num1 > num3:
    print("el numero mayor es:", num1)

elif num2 > num1 and num2 > num3:
    print("el numero mayor es:", num2)

else:
    print("el numero mayor es:", num3)
