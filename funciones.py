
def calculoPrecio(precio, descuento):
    precioFinal = precio - (precio * descuento / 100)
    return precioFinal

def calculoDescuento(precio, precioFinal):
    descuento = ((precio - precioFinal) / precio) * 100
    return descuento

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: ")) 
descuento = float(input("Ingrese el descuento en porcentaje: "))
precioFinal = calculoPrecio(precio, descuento)

print(f"El precio final del producto {producto} es: {precioFinal:.2f}")
