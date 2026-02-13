# Entradas
horas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

# Proceso
if horas <= 40:
    salario = horas * valor_hora
else:
    salario = (40 * valor_hora) + ((horas - 40) * valor_hora * 1.5)

# Salidas
print("El salario total es:", salario)