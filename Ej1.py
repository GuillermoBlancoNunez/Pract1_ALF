import time 

# function that returns the exact time in nanoseconds
def nanoseconds():
    return time.perf_counter_ns()

def a(n: int):
    i = 1
    j = 0
    a = 0
    cnt = 0
    racionales = []
    while cnt < n-1:
        a += 1
        j = a
        if j % 2 == 0:
            while j >= 1:
                racionales.append(str(i)+"/"+str(j))
                j -= 1
                i += 1
                cnt += 1

        else:
            while j >= 1:
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
    racionalesFloat = []
    while cnt < n:
        a += 1
        j = a
        if j % 2 == 0:
            while j >= 1:
                if (i/j) not in racionalesFloat:
                    racionales.append(str(i)+"/"+str(j))
                    racionalesFloat.append(i/j)
                    cnt += 1
                    if cnt >= n:
                        break
                j -= 1
                i += 1
        else:
            while j >= 1:
                if (j/i) not in racionalesFloat:
                    racionales.append(str(j)+"/"+str(i))
                    racionalesFloat.append(j/i)
                    cnt += 1
                    if cnt >= n:
                        break
                j -= 1
                i += 1
        i = 1
    return racionales, racionalesFloat


def main():
    n = int(input("Ingrese el número de dígitos que quiere mostrar: "))
    tipo = input("Ingrese el tipo de lista que quiere mostrar (a/u): ")
    while tipo not in ["a", "u"]:
        print("Tipo no válido")
        tipo = input("Ingrese el tipo de lista que quiere mostrar (a/u): ")
    if tipo == "a":
        t0 = nanoseconds()
        lista = a(n)
        t = nanoseconds() 
        print("Tiempo de ejecución: ", t-t0, "nanosegundos.")
    elif tipo == "u":
        t0 = nanoseconds()
        lista, listaFloat = u(n)
        t = nanoseconds()
        print("Tiempo de ejecución: ", t-t0, "nanosegundos.")
    for i in lista:
        print(i, end=" ")

