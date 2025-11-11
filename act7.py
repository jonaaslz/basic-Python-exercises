#Crea un programa que intente adivinar un número generado de forma aleatoria por el ordenador

import random

num_aleatiorio = random.randint(1, 3)

num_user = int(input("introduce un numero del 1 al 3: "))

if num_user == num_aleatiorio:
    print("¡Felicidades! ¡Has adivinado el número!")

else:
    print("sorry era:",num_aleatiorio ,"prueba otra vez!")