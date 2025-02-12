import time 
import math

# function that returns the exact time in nanoseconds
def nanoseconds():
    return time.perf_counter_ns()

# function to measure the execution time of algorithms
def measure_t(vector, alg):
    t0 = nanoseconds()
    list = alg(vector)  # apply the sorting algorithm
    tf = nanoseconds()
    return (tf-t0), list  # return the elapsed time

def a(n: int):
    i = 1
    j = 0
    a = 0
    cnt = 0
    racionales = []
    while cnt < n:
        a += 1
        j = a
        if j % 2 == 0:
            while j >= 1 and cnt < n:
                racionales.append(str(i)+"/"+str(j))
                j -= 1
                i += 1
                cnt += 1

        else:
            while j >= 1 and cnt < n:
                racionales.append(str(j)+"/"+str(i))
                j -= 1
                i += 1
                cnt += 1
        i = 1
    return racionales


def u(n: int):
    i = 1
    j = 0
    a = 0
    cnt = 0
    racionales = []
    while cnt < n:
        a += 1
        j = a
        if j % 2 == 0:
            while j >= 1 and cnt < n:
                if math.gcd(i, j) == 1:
                    racionales.append(str(i)+"/"+str(j))
                    cnt += 1         
                j -= 1
                i += 1
        else:
            while j >= 1 and cnt < n:
                if math.gcd(i, j) == 1:
                    racionales.append(str(j)+"/"+str(i))
                    cnt += 1         
                j -= 1
                i += 1
        i = 1
    return racionales

def analisis_tiempos():
    t_u, _ = measure_t(1000000, a)
    t_a, _ = measure_t(1000000, u)
    print("__________________________________________________________")
    print("ANÁLISIS DE TIEMPOS")
    print("__________________________________________________________")
    print("\n")
    print(f"Algoritmo a: {t_a} nanosegundos.")
    print(f"Algoritmo u: {t_u} nanosegundos.")
    print("\n")
    print("__________________________________________________________")
    print("\n")
    print(f"El algoritmo u es aproximadamente {round(t_a/t_u,2)} veces más eficiente que el algoritmo a.")
    print("Esto se debe a que u hace una comparación a mayores que comprueba si el numerador y el denominador son primos relativos, y de ser así los añade.")

def menuEj1():
    analisis_tiempos()
    n = int(input("\nIngrese el número de dígitos que quiere mostrar: "))
    tipo = input("\nIngrese el tipo de lista que quiere mostrar (a/u): ")
    while tipo not in ["a", "u"]:
        print("\nTipo no válido")
        tipo = input("\nIngrese el tipo de lista que quiere mostrar (a/u): ")
    if tipo == "a":
        t, lista = measure_t(n, a)
    elif tipo == "u":
        t, lista = measure_t(n, u)
    for i in lista:
        print(i, end=" ")
    print("\nTiempo de ejecución: ", t, "nanosegundos.\n")
