# Solicitar tres notas
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# Proceso
suma = nota1 + nota2 + nota3
promedio = suma / 3

# Salidas
print("El promedio es:", promedio)
if promedio >= 3.0:
    print("Aprueba")
else:
    print("No aprueba")