# Solicitar capital, tasa de interés y tiempo en meses
capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés mensual (%): "))
tiempo = int(input("Ingrese el tiempo en meses: "))

# Proceso
tasa_decimal = tasa / 100
interes_simple = capital * tasa_decimal * tiempo
total_pagar = capital + interes_simple

# Salidas
print("El interés simple es: $", round(interes_simple, 2))
print("El valor total a pagar es: $", round(total_pagar, 2))