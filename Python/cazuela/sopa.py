def lectura(nombre):
    archivo = open(nombre)
    coord = archivo.readline()
    coordenadas = coord.split()
    filas = int(coordenadas[0])
    columnas = int(coordenadas[1])
    matriz=[]
    i = 0
    while i < filas:
        linea = archivo.readline()
        linea = linea.rstrip("\n")
        matriz.append(linea)
        i = i + 1
    cantidad = int(archivo.readline())
    i = 0
    lista = []
    while i < cantidad:
        linea = archivo.readline()
        linea = linea.rstrip("\n")
        lista.append(linea)
        i = i + 1
    archivo.close()
    return matriz, lista, filas, columnas

def procesa_linea(matriz, lista, filas, columnas):
    largo_lista = len(lista)
    palabra = ""
    k = 0
    while k < largo_lista:
        pal = lista[k]
        largo = len(pal)
        fila = 0
        while fila < filas:
            j = 0
            while j + largo -1< columnas:
                p = 0
                palabra = ""
                while p < largo:
                    palabra = palabra + matriz[fila][j+p]
                    p = p + 1
                print "Probando ", palabra, " con ", pal
                if palabra == pal:
                    print "esta en :", fila," , ", j
                j = j + 1
            fila = fila + 1
        k = k + 1

if __name__ == "__main__":
    matriz, lista, filas, columnas = lectura("entrada.txt")
    print "Entrando a procesar....."  
    procesa_linea(matriz, lista, filas, columnas)
    