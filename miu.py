import argparse

def MIU(cadena: str) -> list:
    """
    Genera una lista de posibles modificaciones de la cadena de acuerdo con las reglas del sistema MIU.

    Reglas del sistema MIU:
    - Si la cadena termina en "I", agregar un "U" al final.
    - Si la cadena comienza con "M", duplicar la parte de la cadena después de "M".
    - Si la cadena contiene tres "I" consecutivos, reemplazarlos por un solo "U".
    - Si la cadena contiene dos "U" consecutivos, eliminarlos.

    Args:
    cadena (str): La cadena de entrada sobre la cual se aplican las reglas.

    Returns:
    list: Una lista de cadenas generadas a partir de la cadena original siguiendo las reglas de MIU.
    """
    hijos = []

    # Regla 1: Si termina en "I", agregar "U"
    if cadena[-1] == "I":
        hijos.append(cadena + "U")
        
    # Regla 2: Si comienza con "M", duplicar la parte después de "M"
    if cadena[0] == "M":
        hijos.append(cadena + cadena[1:])
    
    # Regla 3: Reemplazar tres "I" consecutivos por "U"
    for i in range(len(cadena) - 2):
        if cadena[i:i+3] == "III":
            hijos.append(cadena[:i] + "U" + cadena[i+3:])
            
    # Regla 4: Eliminar dos "U" consecutivos
    for i in range(len(cadena) - 1):
        if cadena[i:i+2] == "UU":
            hijos.append(cadena[:i] + cadena[i+2:])
    
    return hijos

def menu():
    """
    Función principal que solicita un número de teoremas a generar, valida la entrada y utiliza 
    la función MIU para generar y mostrar los primeros 'n' teoremas del sistema MIU.

    La entrada debe ser un número entero positivo. Si la entrada es válida, los primeros 'n' teoremas 
    se generan a partir de la cadena inicial "MI". Si la entrada no es válida, se muestra un mensaje de error.

    Args:
    None

    Returns:
    None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("n")
    
    args = parser.parse_args()
    entrada = args.n
    
    if entrada.isdigit():  # Verifica si la entrada es un número entero positivo
        n = int(entrada)
        teoremas = ["MI"]  # único axioma del sistema MIU
        i = 0
        while n > len(teoremas):
            teoremas += MIU(teoremas[i])  # Generar nuevos teoremas
            i += 1
       
        print("\n")
        for i in range(n):
            print(teoremas[i])  # Imprimir los primeros 'n' teoremas

    else:
        print("Error: Entrada no válida. Esta debe ser un número entero positivo.")

def main():
    """
    Función principal que llama a la función menu() para ejecutar el flujo del programa.

    Args:
    None

    Returns:
    None
    """
    menu()

if __name__ == "__main__":
    main()
