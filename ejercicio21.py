# Solicitar capital inicial, tasa de interés y número de períodos
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés por período (%): "))
periodos = int(input("Ingrese el número de períodos: "))

# Proceso
tasa_decimal = tasa / 100
monto_final = capital_inicial * (1 + tasa_decimal) ** periodos

# Salida
print("El monto final es: $", round(monto_final, 2))