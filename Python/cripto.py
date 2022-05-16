def encripta(text, n):
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numer = "0123456789"
    nueva = ""
    for letra in text:
        if letra in minus:
            pos = minus.index(letra)
            nueva = nueva + minus[(pos + n)%26]
        if letra in mayus:
            pos = mayus.index(letra)
            nueva = nueva + mayus[(pos + n)%26]       
        if letra in numer:
            pos = numer.index(letra)
            nueva = nueva + numer[(pos + n)%10]  
    return nueva
    
def desencripta(text, n):
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numer = "0123456789"
    nueva = ""
    for letra in text:
        if letra in minus:
            pos = minus.index(letra)
            nueva = nueva + minus[(pos - n)%26]
        if letra in mayus:
            pos = mayus.index(letra)
            nueva = nueva + mayus[(pos - n)%26]       
        if letra in numer:
            pos = numer.index(letra)
            nueva = nueva + numer[(pos - n)%10]  
    return nueva    

if __name__ == "__main__":
    frase = input("Frase: ")
    n = int(input("n: "))
    nueva_frase = encripta(frase, n)
    vieja_frase = desencripta(nueva_frase, n)
    print ("Original: ", frase)
    print ("Encriptada: ", nueva_frase)
    print ("Desencriptada: ", vieja_frase)
    