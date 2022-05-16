def digito_verificador(rut):
    constantes = [7,6,5,4,3,2,7,6,5,4,3,2]
    l = len(rut)*-1
    i = -1
    suma = 0
    while i >= l:
        suma = suma + int(rut[i])*constantes[i]
        i = i - 1
    resul = suma % 11
    resul = 11 - resul
    if resul == 11:
        digito = "0"
    elif resul == 10:
        digito = "K"
    else:
        digito = str(resul)
    return digito

if __name__ == "__main__":
    rut = "12678579"
    dv = digito_verificador(rut)
    print dv
    
        