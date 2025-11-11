#Cuenta las vocales de una palabra

palabra = input("introduce una palabra: ")

vocales = "aeiouAEIOU"

contador = 0


for caracter in palabra:
    if caracter in vocales:
        contador += 1

print("la palabra tiene", contador, "vocales")