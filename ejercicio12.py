print("\n--- Ejercicio 12: Comisión escalonada ---")
ventas = float(input("Ingrese el valor de ventas mensuales: $"))
if ventas > 1000000:
    comision = ventas * 0.10
    porcentaje = "10%"
else:
    comision = ventas * 0.05
    porcentaje = "5%"
print(f"La comisión es del {porcentaje}: ${comision:,.2f}")