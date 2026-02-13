# Solicitar valor en pesos colombianos y tasa de cambio
pesos = float(input("Ingrese el valor en pesos colombianos: "))
tasa_dolar = float(input("Ingrese la tasa de cambio (1 dólar = ? pesos): "))

# Proceso
dolares = pesos / tasa_dolar

# Salida
print("El valor en dólares es: $", round(dolares, 2), "USD")