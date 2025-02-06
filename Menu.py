
from Ej1 import main as Ej1_main
from Ej2 import main as Ej2_main
from Ej3 import main as Ej3_main

def mostrarMenu():
    while True:
        try:
            n = int(input("Ingrese el ejercicio que quiera ejecutar (1-3): "))
            if n in [1, 2, 3]:
                break
            else:
                print("Error: Debe introducir un número entre 1 y 3.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    ejecutar = [Ej1_main(), Ej2_main(), Ej3_main()]
    ejecutar[n-1]



