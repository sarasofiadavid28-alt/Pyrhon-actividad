# EJERCICIO 10 - TOTAL DE COMPRA CON VARIOS PRODUCTOS

print("\n=== EJERCICIO 10: TOTAL DE COMPRA ===\n")

try:
    # Entrada
    cantidad = int(input("¿Cuántos productos compró?: "))

    if cantidad <= 0:
        print("\nError: La cantidad debe ser mayor a 0")
    else:
        total = 0

        # Proceso
        for i in range(cantidad):
            precio = float(input(f"Ingrese el precio del producto {i+1}: "))
            total += precio

        # Salida
        print(f"\nEl total de la compra es: ${total:.2f}")

except ValueError:
    print("\nError: Debe ingresar valores numéricos válidos")
