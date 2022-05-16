def primo(n):
    es = False
    for i in range(2, n, 1):
        print(i)
        if (n%i) == 0:
            es = True
    return es

if __name__ == "__main__":
    n = int(input("Numero a determinar si es primo: "))
    es_primo = primo(n)
    if es_primo:
        print("Es compuesto")
    else:
        print("Es Primo")
