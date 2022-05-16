def lectura(nombre):
    t = []
    p = []
    archi = open(nombre)
    linea = archi.readline()
    indices = linea.split()
    fil = int(indices[0])
    col = int(indices[1])
    i = 0
    while i < fil:
        linea = archi.readline()
        linea = linea.rstrip("\n")
        t.append(linea)
        i = i + 1
    cant = int(archi.readline())
    i = 0
    while i < cant:
        palabra = archi.readline()
        palabra = palabra.rstrip("\n")
        p.append(palabra)
        i = i + 1
    archi.close()
    return t,p,fil,col

def escribir(salida):
    archi = open("salida.txt", "w")
    for linea in salida:
        archi.writelines(linea)
        archi.writelines("\n")
    archi.close()
        
if __name__ == "__main__":
    tablero, palabras, filas, columnas = lectura("entrada.txt")
    print tablero
    print palabras
    print filas
    print columnas
    salida = ["3 5 3 2", "3 4 3 1", "3 2 3 4", "2 3 5 3","? ? ?","3 1 5 3"]
    escribir(salida)
    