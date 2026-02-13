# Entradas
cantidad = int(input("¿Cuántos productos compró?: "))

# Proceso
total = 0
for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del producto {i+1}: "))
    total = total + precio

# Salidas
print("El total de la compra es:", total)