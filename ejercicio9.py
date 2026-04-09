# EJERCICIO 9 - CÁLCULO DE IVA

print("\n=== EJERCICIO 9: CÁLCULO DE IVA (19%) ===\n")

try:
    # Entrada
    venta = float(input("Ingrese el valor de la venta sin IVA: "))

    # Proceso
    iva = venta * 0.19
    total = venta + iva

    # Salida
    print(f"\nValor de la venta: ${venta:.2f}")
    print(f"IVA (19%): ${iva:.2f}")
    print(f"Total a pagar: ${total:.2f}")

except ValueError:
    print("\nError: Debe ingresar un valor numérico válido")
