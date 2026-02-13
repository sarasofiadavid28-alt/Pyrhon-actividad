# index.py
# creado por
import os # interactua operando (archivos,directorios,rutas,variables de entorno)
import sys
import subprocess





while True:
    print("=============================")
    print("taller 1 - Algortimos basicos en python")
    print("by carlos andres castro jaramillo")
    print("menu principal")
    print("=============================")
    
    for i in range(1,26):
        print(f"{i}. Ejecutar ALgoritmo{i}")
    print("0.salir\n")
    
    opcion = input("seleccione una opcion: ")
    
    if opcion == "0":
        print("saliendo...")
        break
    
    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"ejercicio{opcion}.py"
        
        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
            input("\nPresione Enter para continuar...")
        else:
            print("Archivo no encontrado")
    else:
        print("Opcion no valida")

