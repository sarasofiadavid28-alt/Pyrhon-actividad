
# Solicitar el peso del paquete
peso = float(input("Ingrese el peso del paquete en kg: "))

# Proceso
if peso <= 5:
    costo_envio = 10000
else:
    costo_envio = 20000

# Salida
print("El valor del envío es: $", costo_envio)