def producir(cad:str)->str:
    for i in cad:
        if i == "g":
            cad = cad[:cad.index(i)] + "~" + cad[cad.index(i):] + "~"
    return cad

def axioma(i: int)->str:
    return (i * "~") + "m~g" + (i * "~") + "~"


def mg(n: int)->list:
    coleccion = []
    orden = []
    i = 0
    while len(coleccion) < n:
        s = axioma(i)
        coleccion.append(s)
        orden.append(s)
        c = producir(orden.pop(0))
        coleccion.append(c)
        orden.append(c)
        i += 1


    return coleccion

def pedirNum()->int:
    while True:
        try:
            n = int(input("\nIngrese la cantidad de teoremas a generar: "))

                        
        except ValueError:
            print("\nError: Debe ingresar un número válido.")
        else:
            return n

        

def main()->None:
    n = pedirNum()
    teoremas = mg(n)
    for i in range(n):
        print(teoremas[i])
    correct = ["m∼g∼", "m∼∼g∼∼", "∼m∼g∼∼", "m∼∼∼g∼∼∼", "∼m∼∼g∼∼∼", "∼∼m∼g∼∼∼", "m∼∼∼∼g∼∼∼∼", "∼m∼∼∼g∼∼∼∼", "∼∼m∼∼g∼∼∼∼", "∼∼∼m∼g∼∼∼∼", "m∼∼∼∼∼g∼∼∼∼∼", "∼m∼∼∼∼g∼∼∼∼∼", "∼∼m∼∼∼g∼∼∼∼∼", "∼∼∼m∼∼g∼∼∼∼∼", "∼∼∼∼m∼g∼∼∼∼∼"]


if __name__ == "__main__":
    main()
    ["m∼g∼", "m∼∼g∼∼", "∼m∼g∼∼", "m∼∼∼g∼∼∼", "∼m∼∼g∼∼∼", "∼∼m∼g∼∼∼", "m∼∼∼∼g∼∼∼∼", "∼m∼∼∼g∼∼∼∼", "∼∼m∼∼g∼∼∼∼", "∼∼∼m∼g∼∼∼∼", "m∼∼∼∼∼g∼∼∼∼∼", "∼m∼∼∼∼g∼∼∼∼∼", "∼∼m∼∼∼g∼∼∼∼∼", "∼∼∼m∼∼g∼∼∼∼∼", "∼∼∼∼m∼g∼∼∼∼∼"]