# Solicitar la edad de la persona
edad = int(input("Ingrese su edad: "))

# Proceso
if edad < 18:
    clasificacion = "Menor de edad"
elif edad >= 18 and edad < 60:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto mayor"

# Salida
print("Clasificación:", clasificacion)