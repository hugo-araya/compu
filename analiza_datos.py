import matplotlib.pyplot as plt

def lectura(nombre):
    ar = open(nombre)
    datos = []
    for linea in ar:
        linea = linea.rstrip("\n")
        lista = linea.split(",")
        datos.append(lista) 
    return datos

def separaporagno(datos):
    lista = []
    for elem in datos:
        lista.append(int(elem[3]))
    return lista

def juntaporagno(lista):
    x = []
    y = []
    lista.sort()
    for elem in lista:
        if elem not in x:
            x.append(elem)
    for elem in x:
        numero = lista.count(elem)
        y.append(numero)
    return x, y

def graficar(x, y):
    plt.bar(x,y, width=1, edgecolor="white", linewidth=0.7)
    #plt.pie(y)
    plt.show()

if __name__ == "__main__":
    datos = lectura("personas.txt")
    lista1 = separaporagno(datos)
    x, y = juntaporagno(lista1)
    graficar(x, y)