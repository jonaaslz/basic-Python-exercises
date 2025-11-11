#Suma, resta, multiplicación y división dos números que se introduzcan por teclado.

numero1 = int(input("introduce tu primer número: "))
numero2 = int(input("introduce tu segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(" que quieres hacer?: suma, resta, multiplicación o división")

operacion = input("elige una operación: ")

if operacion == "suma":
    print("el resultado de la suma es:", suma)

elif operacion == "resta":
    print ("el resultado de la resta es:", resta)

elif operacion == "multiplicacion":
    print("el resultado de la multiplicación es:", multiplicacion)

elif operacion == "division":
    print("el resultado de la división es:", division)

else: 
    print("prueba otra vez")