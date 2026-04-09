# EJERCICIO 4 - CÁLCULO DE SALARIO SEMANAL

print("\n=== EJERCICIO 4: SALARIO SEMANAL ===\n")

try:
    # Entradas
    horas = float(input("Ingrese las horas trabajadas en la semana: "))
    valor_hora = float(input("Ingrese el valor por hora: "))

    # Proceso
    salario = horas * valor_hora

    # Salida
    print(f"\nEl salario semanal es: ${salario:.2f}")

except ValueError:
    print("\nError: Debe ingresar valores numéricos")
