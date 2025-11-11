#Lista de compras: Pide varios artículos y almacénalos para mostrarlos al final. #no lo entiendo
lista_compras = []
while True:

    articulo = input("Introduce un artículo para la lista de compras (o 'salir' para terminar): ")
    if articulo.lower() == 'salir':
        break

    lista_compras.append(articulo)
print("Tu lista de compras es:")

for item in lista_compras:
    print("-", item)