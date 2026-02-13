# Entradas
compra = float(input("Ingrese el valor de la compra: "))

# Proceso
if compra > 100000:
    descuento = compra * 0.10
    total = compra - descuento
    print("Se aplicó descuento del 10%")
    print("Valor del descuento:", descuento)
else:
    total = compra

# Salidas
print("Total a pagar:", total)