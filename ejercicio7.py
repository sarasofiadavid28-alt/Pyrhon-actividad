# EJERCICIO 7 - MAYOR O MENOR DE EDAD

print("\n=== EJERCICIO 7: VALIDACIÓN DE EDAD ===\n")

try:
    # Entrada
    edad = int(input("Ingrese su edad: "))

    # Proceso y salida
    if edad >= 18:
        print(f"\nUsted es MAYOR de edad ({edad} años)")
    else:
        print(f"\nUsted es MENOR de edad ({edad} años)")

except ValueError:
    print("\nError: Debe ingresar una edad válida")
