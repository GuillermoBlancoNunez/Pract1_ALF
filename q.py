import argparse
import time 
import math
from typing import Tuple



def nanoseconds() -> int:
    """
    Returns the current time in nanoseconds using time.perf_counter_ns().
    
    Returns:
    int: Current time in nanoseconds.
    """
    return time.perf_counter_ns()

def measure_t(n: int, alg) -> Tuple[int, list]: 
    """
    Measures the execution time of a specified algorithm applied to a vector.

    Args:
    n (int): The size of the vector or input to the algorithm.
    alg (function): The algorithm function to measure.

    Returns:
    tuple: A tuple containing the elapsed time in nanoseconds and the result of the algorithm.
    """
    t0 = nanoseconds()
    result = alg(n)  
    tf = nanoseconds()
    return (tf - t0), result

def a(n: int) -> list:
    """
    Generates a list of rational numbers as strings up to 'n' entries,
    where each entry is in the form 'numerator/denominator'.

    Args:
    n (int): Number of rational numbers to generate.

    Returns:
    list: List of 'n' rational numbers as strings.
    """
    i = 1
    j = 0
    a = 0
    cnt = 0
    rationals = []
    while cnt < n:
        a += 1
        j = a
        if j % 2 == 0:
            while j >= 1 and cnt < n:
                rationals.append(str(i)+"/"+str(j))
                j -= 1
                i += 1
                cnt += 1
        else:
            while j >= 1 and cnt < n:
                rationals.append(str(j)+"/"+str(i))
                j -= 1
                i += 1
                cnt += 1
        i = 1
    return rationals

def u(n: int) -> list:
    """
    Generates a list of simplified rational numbers as strings up to 'n' entries,
    where each entry is in the form 'numerator/denominator' and only includes numbers
    where the numerator and denominator are coprime.

    Args:
    n (int): Number of rational numbers to generate.

    Returns:
    list: List of 'n' simplified rational numbers as strings.
    """
    i = 1
    j = 0
    a = 0
    cnt = 0
    rationals = []
    while cnt < n:
        a += 1
        j = a
        if j % 2 == 0:
            while j >= 1 and cnt < n:
                if math.gcd(i, j) == 1:
                    rationals.append(str(i)+"/"+str(j))
                    cnt += 1         
                j -= 1
                i += 1
        else:
            while j >= 1 and cnt < n:
                if math.gcd(i, j) == 1:
                    rationals.append(str(j)+"/"+str(i))
                    cnt += 1         
                j -= 1
                i += 1
        i = 1
    return rationals

def analisis_tiempos() -> None:
    """
    Measures and compares the execution times of functions 'a' and 'u' for generating
    lists of rational numbers. Prints an analysis summary of the times and efficiencies.
    """
    t_a, _ = measure_t(1000000, a)
    t_u, _ = measure_t(1000000, u)
    print("__________________________________________________________")
    print("ANÁLISIS DE TIEMPOS")
    print("__________________________________________________________")
    print("\n")
    print("Para n = 1000000")
    print(f"Algoritmo a: {t_a} nanosegundos.")
    print(f"Algoritmo u: {t_u} nanosegundos.")
    print("\n")
    print("__________________________________________________________")
    print("\n")
    print(f"El algoritmo a es aproximadamente {round(t_u/t_a,2)} veces más eficiente que el algoritmo u.")
    print("Esto se debe a que u hace una comparación adicional que comprueba si el numerador y el denominador son primos relativos, y de ser así los añade.")
    print("__________________________________________________________")
    print("\n")

def menu() -> None:
    """
    Executes an analysis of execution times between functions 'a' and 'u', and allows the user
    to choose the type ('a' or 'u') and number of rational numbers to generate. Displays the
    generated list and the execution time for the chosen function.
    """
    parser = argparse.ArgumentParser()
    
    # Definir opciones con guiones
    parser.add_argument("-a", "--alg-a", action="store_true")
    parser.add_argument("-u", "--alg-u", action="store_true")
    parser.add_argument("n", type=int)

    args = parser.parse_args()

    # Verificar qué opción se usó
    if args.alg_a:
        t, result = measure_t(args.n, a)
    elif args.alg_u:
        t, result = measure_t(args.n, u)
    else:
        print("Error: Debes especificar -a o -u")
        return

    analisis_tiempos()

    # Imprimir resultados
    print("\t".join(result))
    print(f"\nTiempo de ejecución: {t} nanosegundos.\n")

def main() -> None:
    """
    Main function that executes the menu function.
    """
    menu()

if __name__ == "__main__":
    main()
