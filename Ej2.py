def producir(cad:str)->str:
    return cad[:cad.index("g")] + "~" + cad[cad.index("g"):] +"~"
    

def axioma(i: int)->str:
    return (i * "~") + "m~g" + (i * "~") + "~"


def mg(n: int)->list:
    coleccion = []
    orden = []
    i = 0
    while len(coleccion) < n:
        s = axioma(i)
        i += 1
        coleccion.append(s)
        orden.append(s)
        c = producir(orden.pop(0))
        coleccion.append(c)
        orden.append(c)

    return coleccion

def pedirNumCantidad()->int:
    while True:
        try:
            n = int(input("\nIngrese la cantidad de teoremas a generar: "))

        except ValueError:
            print("\nError: Debe ingresar un número válido.")
        else:
            return n

def mgCheck(cad:str):
    
    i = cad.index("m")
    if cad == axioma(len(cad[:i])):
        return "yes"
    elif len(cad) > 4 and len(cad)% 2 == 0:
        newCad = cad[:cad.index("g")-1] + cad[cad.index("g"):len(cad)-1]
        return mgCheck(newCad)
        
    return "no"


def pedirNumFuncion():
    while True:
        try:
            n = int(input("\nIngrese la funcionalidad del ejercicio que quiere utilizar (1-2):\n1. Generar n número de modelos.\n2. Comprobrar si un posible teorema forma parte del sistema formal mg~\n "))
            if n in [1, 2]:
                break
            else:
                print("\nError: Debe introducir un número entre 1 y 2.")
        except ValueError:
            print("\nError: Debe ingresar un número válido.")

    return n


def main()->None:
    f = pedirNumFuncion()
    if f == 1:
        n = pedirNumCantidad()
        teoremas = mg(n)
        for i in range(n):
            print(teoremas[i])
    elif f ==2:
        s = str(input("Introduzca la cadena que quiera comprobar si está en el sistema formal mg~\n"))
        print(mgCheck(s))
            


if __name__ == "__main__":
    main()