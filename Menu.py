
from Ej1 import main as Ej1_main
from Ej2 import main as Ej2_main
from Ej3 import main as Ej3_main

def mostrarMenu():
    while True:
        try:
            n = int(input("\nIngrese el ejercicio que quiera ejecutar (1-3): "))
            if n in [1, 2, 3]:
                break
            else:
                print("\nError: Debe introducir un número entre 1 y 3.")
        except ValueError:
            print("\nError: Debe ingresar un número válido.")
    ejecutar = [Ej1_main, Ej2_main, Ej3_main]
    ejecutar[n-1]()



