# Solicitar número de ventas
num_ventas = int(input("Ingrese el número de ventas realizadas en el día: "))

# Proceso
total_vendido = 0
for i in range(num_ventas):
    valor_venta = float(input(f"Ingrese el valor de la venta {i+1}: $"))
    total_vendido = total_vendido + valor_venta

promedio_venta = total_vendido / num_ventas

# Salidas
print("El total vendido en el día es: $", round(total_vendido, 2))
print("El promedio por venta es: $", round(promedio_venta, 2))