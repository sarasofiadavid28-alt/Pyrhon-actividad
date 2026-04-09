# EJERCICIO 3 - CONVERSIÓN DE CELSIUS A FAHRENHEIT

print("\n=== EJERCICIO 3: CONVERSIÓN DE TEMPERATURA ===\n")

try:
    # Entrada
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))

    # Proceso
    fahrenheit = (celsius * 9/5) + 32

    # Salida
    print(f"\nLa temperatura en Fahrenheit es: {fahrenheit:.2f}")

except ValueError:
    print("\nError: Debe ingresar un número válido")
