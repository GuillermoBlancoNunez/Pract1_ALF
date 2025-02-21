import argparse
import math
def MIU(cadena="MI"):
    """
    Genera las posibles cadenas derivadas de una cadena dada siguiendo las reglas del sistema MIU.
    
    Reglas del sistema MIU:
    - Si la cadena termina en "I", agregar un "U".
    - Si la cadena comienza con "M", duplicar la parte después de "M".
    - Si la cadena contiene tres "I" consecutivos, reemplazarlos por un solo "U".
    - Si la cadena contiene dos "U" consecutivas, eliminarlas.
    
    Args:
    cadena (str): La cadena sobre la cual aplicar las reglas.
    
    Returns:
    list: Lista con las cadenas generadas a partir de la cadena dada.
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


def no_repeat_MIU(n: int, cadena_inicial="MI"):
    """
    Genera hasta 'n' cadenas únicas del sistema MIU sin repeticiones, usando BFS y el método MIU para aplicar las reglas.
    
    Args:
    cadena_inicial (str): La cadena inicial (ejemplo: "MI").
    - n (int): Número máximo de cadenas a generar.

    Returns:
    list: Lista con hasta 'n' cadenas únicas generadas según las reglas del sistema MIU.
    """


    visitadas = set([cadena_inicial])  # Usamos un set para evitar repeticiones
    resultado = [cadena_inicial]       # Almacena las cadenas generadas
    cola = [cadena_inicial]     # BFS: Cola de cadenas a explorar

    while cola and len(resultado) < n:
        cadena = cola.pop(0)

        # Usar el método MIU para aplicar las reglas y obtener las nuevas cadenas
        posibles_cadenas = MIU(cadena)

        # Añadir las nuevas cadenas a la cola si no han sido visitadas
        for nueva_cadena in posibles_cadenas:
            if nueva_cadena not in visitadas:
                visitadas.add(nueva_cadena)
                cola.append(nueva_cadena)
                resultado.append(nueva_cadena)
                if len(resultado) == n:
                    break

    return resultado


def decision_MIU(cad: str) -> str:
    """
    Determina si una cadena dada es un teorema válido del sistema MIU.

    Args:
    cadena (str): La cadena a evaluar.

    Returns:
    str: "yes" si la cadena es un teorema válido, "no" en caso contrario.
    """
    if cad == "MI":
        return True
    nI = cad.count("I")
    nM = cad.count("M")
    nU = cad.count("U")
    if nI < 1 or nM != 1 or cad.index("M") != 0:
        return False
    
    subcad = cad[1:]
    if len(subcad) % 2 == 0:
        medio = len(subcad) // 2
        if subcad[:medio] == subcad[medio:]:
            return decision_MIU("M" + subcad[:medio])
        
    if cad[len(cad)-2:] == "IU":
        return decision_MIU(cad[:len(cad)-1])
   
    if "UU" in cad:
        return decision_MIU(cad.replace("UU", ""))

    cad = cad.replace("U", "III")

    n = len(cad[1:])
    if n > 0 and math.log2(n).is_integer():
        return True
    else:
        return False

        

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
    parser.add_argument("x")
    parser.add_argument("-NoRepeat", "--alg-NoRepeat", action="store_true")
    
    args = parser.parse_args()
    entrada = args.x

    if entrada.isdigit():
        if args.alg_NoRepeat:
          # Verifica si la entrada es un número entero positivo
            n = int(entrada)
            cadenas = no_repeat_MIU(n)
            for cadena in cadenas:
                print(cadena)

        else:  # Verifica si la entrada es un número entero positivo
            n = int(entrada)
            teoremas = ["MI"]  # único axioma del sistema MIU
            i = 0
            while n > len(teoremas):
                teoremas += MIU(teoremas[i])  # Generar nuevos teoremas
                i += 1
        
            print("\n")
            check = True
            #for i in range(n):
            i=-1
            while i < n:
                i += 1
                print(teoremas[i])  # Imprimir los primeros 'n' teoremas
                if decision_MIU(teoremas[i]) == False:
                    check = False
                    print(teoremas[i])
                    print("ala")
                                      

            print("La implementacion de decision", check)

    elif all(letra in "MIU" for letra in entrada) and "M" in entrada and "I" in entrada :
        print(decision_MIU(entrada))

    else:
        print("Error: Entrada no válida. Esta debe ser un número entero positivo o una cadena que solo contenga los caracteres M, I y U.")

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
