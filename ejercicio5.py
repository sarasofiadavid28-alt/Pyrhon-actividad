# EJERCICIO 5 - CÁLCULO DE SALARIO CON HORAS EXTRA

print("\n=== EJERCICIO 5: SALARIO CON HORAS EXTRA ===\n")

try:
    # Entradas
    horas = float(input("Ingrese las horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor por hora: "))

    # Proceso
    if horas <= 40:
        salario = horas * valor_hora
    else:
        horas_extra = horas - 40
        salario = (40 * valor_hora) + (horas_extra * valor_hora * 1.5)

    # Salida
    print(f"\nEl salario total es: ${salario:.2f}")

except ValueError:
    print("\nError: Debe ingresar valores numéricos")
