

# Diccionario con productos y sus precios
productos = {
    "shampoo": 5,
    "jabón": 3,
    "pasta dental": 4,
    "crema corporal": 10,
    "peine": 2
}

# Pedir al usuario que seleccione un producto
producto_seleccionado = input("Ingrese el nombre del producto: ")

# Verificar si el producto está en el diccionario
if producto_seleccionado in productos:

    cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado}: "))

    precio_total = cantidad * productos[producto_seleccionado]

    print(f"El total por {cantidad} {producto_seleccionado}(s) es: {precio_total} dólares.")
    
else:
    print("El producto ingresado no está en la lista.")



