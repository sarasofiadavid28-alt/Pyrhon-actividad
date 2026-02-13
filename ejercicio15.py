# Solicitar dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Proceso
if num1 > num2:
    resultado = "El mayor es: " + str(num1)
elif num2 > num1:
    resultado = "El mayor es: " + str(num2)
else:
    resultado = "Los números son iguales"

# Salida
print(resultado)