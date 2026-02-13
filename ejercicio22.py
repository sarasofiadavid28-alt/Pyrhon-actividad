# Solicitar cantidad inicial, vendida y recibida
inicial = int(input("Ingrese la cantidad inicial del producto: "))
vendida = int(input("Ingrese la cantidad vendida: "))
recibida = int(input("Ingrese la cantidad recibida: "))

# Proceso
inventario_final = inicial - vendida + recibida

# Salida
print("El inventario final es:", inventario_final, "unidades")