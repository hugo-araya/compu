import matplotlib.pyplot as plt

def lectura(nombre):
    ar = open(nombre)
    datos = []
    for linea in ar:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    return datos

def rescataagnos(lista):
    agnos = []
    for elem in lista:
        if int(elem[2]) >= 1 and int(elem[2]) <= 12:
            agnos.append(int(elem[-1]))
    agnos.sort()
    return agnos

def paragraficar(agnos):
    x = []
    y = []
    for elem in agnos:
        if elem not in x:
            x.append(elem)
    for elem in x:
        contar = agnos.count(elem)
        y.append(contar)
    return x, y

def graficar(x, y):
    plt.bar(x,y, width=0.5, edgecolor="red", linewidth=1.0)
    plt.pie(y)
    plt.show()

if __name__ == "__main__":
    datos = lectura('personas.txt')
    agnos = rescataagnos(datos)
    x, y = paragraficar(agnos)
    graficar(x, y)


