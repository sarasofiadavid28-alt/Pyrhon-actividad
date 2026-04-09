# index.py

import os
import sys
import subprocess


def mostrar_menu():
    print("\n" + "=" * 40)
    print("TALLER 1 - ALGORITMOS BÁSICOS EN PYTHON")
    print("Autor: Carlos Andres Castro Jaramillo")
    print("=" * 40)
    print("MENÚ PRINCIPAL\n")

    for i in range(1, 26):
        print(f"{i}. Ejecutar algoritmo {i}")

    print("0. Salir\n")


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "0":
        print("\nSaliendo del sistema...")
        break

    # Validación clara
    if not opcion.isdigit():
        print("❌ Debe ingresar un número")
        continue

    opcion_num = int(opcion)

    if 1 <= opcion_num <= 25:
        archivo = f"ejercicio{opcion}.py"

        if os.path.exists(archivo):
            print(f"\n=== EJECUTANDO ALGORITMO {opcion} ===\n")
            subprocess.run([sys.executable, archivo])
            input("\nPresione Enter para continuar...")
        else:
            print("❌ Archivo no encontrado")
    else:
        print("❌ Opción fuera de rango")
