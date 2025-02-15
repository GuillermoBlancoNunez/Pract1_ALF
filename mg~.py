import argparse
from typing import List

def producir(cad: str) -> str:
    """
    Modifica una cadena introducida, añadiendo un "~" justo antes de la "g" y añadiendo otro al final de la cadena.

    Args:
    cad (str): La cadena de entrada que será procesada.

    Returns:
    str: La cadena nueva, producida a partir de una cadena que ya formaba parte del sistema formal.
    """

    return cad[:cad.index("g")] + "~" + cad[cad.index("g"):] +"~"


def axioma(i: int) -> str:
    """
    Genera una cadena inicial basada en un número dado.

    Args:
    i (int): Número de '~' a agregar en ambos extremos de la cadena base "m~g" y antes del final "~".

    Returns:
    str: La cadena generada.
    """
    return (i * "~") + "m~g" + (i * "~") + "~"


def mg(n: int) -> List[str]:
    """
    Genera una colección de teoremas aplicando reglas de producción.

    Args:
    n (int): Número de teoremas a generar.

    Returns:
    List[str]: Una lista con las cadenas generadas según las reglas de producción.
    """
    coleccion = []
    orden = []
    i = 0

    while len(coleccion) < n:
        s = axioma(i)  # Genera la cadena inicial
        coleccion.append(s)  # Agrega el axioma a la colección
        orden.append(s)  # Se añade a la lista de procesamiento

        # Aplica la regla de producción y almacena el resultado
        c = producir(orden.pop(0))
        coleccion.append(c)
        orden.append(c)

        i += 1  # Incrementa el índice para el siguiente axioma

    return coleccion


def validate(cad: str) -> str:
    """
    Valida una cadena de texto siguiendo las reglas de producción.

    Args:
    cad (str): La cadena de texto a validar.

    Returns:
    str: "yes" si la cadena es válida, "no" en caso contrario.
    """
    
    i = cad.index("m")
    if cad == axioma(len(cad[:i])):
        return "yes"
    elif len(cad) > 4 and len(cad)% 2 == 0:
        newCad = cad[:cad.index("g")-1] + cad[cad.index("g"):len(cad)-1]
        return validate(newCad)

    return "no"
   

       
    
    

def menu() -> None:
    """
    Función principal que ejecuta la generación de teoremas o valida la cadena de texto.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("entrada")
    
    args = parser.parse_args()
    entrada = args.entrada
    
    if entrada.isdigit():  # Verifica si la entrada es un número entero positivo
        n = int(entrada)
        teoremas = mg(n)

        for i in range(n):
            print(teoremas[i])
    
    elif all(i in "~mg" for i in entrada) :  # Verifica si la cadena solo contiene ~, m, g
        print(validate(entrada))
     
    else:
        print("Error: Entrada no válida. Esta debe ser un número entero positivo o una cadena que solo contenga los caracteres ~, m, y g.")

def main() -> None:
    """
    Función principal que ejecuta la generación de teoremas y los muestra en pantalla
    o comprueba su validez.
    """
    menu()

if __name__ == "__main__":
    main()