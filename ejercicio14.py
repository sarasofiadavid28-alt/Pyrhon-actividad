# Solicitar las tres notas
talleres = float(input("Ingrese la nota de talleres (30%): "))
examen_parcial = float(input("Ingrese la nota del examen parcial (30%): "))
examen_final = float(input("Ingrese la nota del examen final (40%): "))

# Proceso
nota_talleres = talleres * 0.30
nota_parcial = examen_parcial * 0.30
nota_final = examen_final * 0.40
nota_definitiva = nota_talleres + nota_parcial + nota_final

# Salida
print("La nota definitiva es:", nota_definitiva)