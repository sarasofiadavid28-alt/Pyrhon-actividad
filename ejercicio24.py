# Solicitar consumo de agua y valor por metro cúbico
consumo = float(input("Ingrese el consumo de agua en metros cúbicos (m³): "))
valor_m3 = float(input("Ingrese el valor por metro cúbico: $"))

# Proceso
valor_total = consumo * valor_m3

# Salida
print("El valor total de la factura es: $", round(valor_total, 2))