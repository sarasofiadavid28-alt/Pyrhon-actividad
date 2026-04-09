# EJERCICIO 2 - CÁLCULO DEL ÁREA DE UN RECTÁNGULO

print("\n=== EJERCICIO 2: ÁREA DE UN RECTÁNGULO ===\n")

try:
    # Solicitar datos
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    # Calcular área
    area = base * altura

    # Mostrar resultado
    print(f"\nEl área del rectángulo es: {area}")

except ValueError:
    print("\n❌ Error: Debe ingresar valores numéricos")
