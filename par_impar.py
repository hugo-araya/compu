
def par(n):
    if n == 0:
        return True
    return impar(n-1)

def impar(n):
    if n == 0:
        return False 
    return par(n-1)

if __name__ == "__main__":
    print(par(12))

