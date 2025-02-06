def producir(cad:str)->str:
    for i in cad:
        if i == "g":
            cad = cad[:cad.index(i)] + "~" + cad[cad.index(i):] + "~"
    return cad

def axioma(i: int)->str:
    return (i * "~") + "m~g" + (i * "~") + "~"


def mg(n: int):
    coleccion = []
    
    return 
def main()->None:
    coleccion = []


if __name__ == "__main__":
    main()