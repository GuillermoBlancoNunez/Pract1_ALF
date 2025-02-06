def MIU(cadena: str) -> list:
    letras = [letra for letra in cadena]
    hijos = []

    if letras[-1] == "I":
        hijos.append("".join(letras + ["U"]))
        
    if letras[0] == "M":
        hijos.append("".join(letras + letras[1:]))
    
    for i in range(0, len(letras)):
        j = i + 3
        if ["I", "I", "I"] == letras[i:j]:
            hijos.append("".join(letras[:i] + ["U"] + letras[j:]))
            
    for i in range(0, len(letras)):
        j = i + 2
        if ["U", "U"] == letras[i:j]:
            hijos.append("".join(letras[:i] + letras[j:]))
            
    
    return hijos

def main():
    n = int(input("Ingrese la cantidad de teoremas a generar: "))
    teoremas = ["MI"]
    i = 0
    while n > len(teoremas):
        teoremas += MIU(teoremas[i])
        i += 1
    print(teoremas[:n])








