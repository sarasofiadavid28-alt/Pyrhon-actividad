# EJERCICIO 6 - NÚMERO PAR O IMPAR

print("\n=== EJERCICIO 6: PAR O IMPAR ===\n")

try:
    # Entrada
    numero = int(input("Ingrese un número entero: "))

    # Proceso y salida
    if numero % 2 == 0:
        print(f"\nEl número {numero} es PAR")
    else:
        print(f"\nEl número {numero} es IMPAR")

except ValueError:
    print("\nError: Debe ingresar un número entero válido")
