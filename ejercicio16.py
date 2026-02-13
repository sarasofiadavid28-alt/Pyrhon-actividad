# Solicitar un número entero
numero = int(input("Ingrese un número entero: "))

# Proceso
if numero % 2 == 0:
    resultado = "El número es par"
else:
    resultado = "El número es impar"

# Salida
print(resultado)