# EJERCICIO 8 - DESCUENTO EN COMPRA

print("\n=== EJERCICIO 8: DESCUENTO POR COMPRA ===\n")

try:
    # Entrada
    compra = float(input("Ingrese el valor de la compra: "))

    # Proceso
    if compra > 100000:
        descuento = compra * 0.10
        total = compra - descuento

        print("\nSe aplicó un descuento del 10%")
        print(f"Valor del descuento: ${descuento:.2f}")
    else:
        descuento = 0
        total = compra
        print("\nNo aplica descuento")

    # Salida
    print(f"Total a pagar: ${total:.2f}")

except ValueError:
    print("\nError: Debe ingresar un valor numérico válido")
