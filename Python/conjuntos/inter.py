def interseccion(l1, l2):
    l3 = []
    for elem in l1:
        if elem in l2:
            if not elem in l3:
                l3.append(elem)
    return l3

def union(l1,l2):
    l3 = []
    for elem in l1:
        l3.append(elem)
    for elem in l2:
        if not elem in l3:
            l3.append(elem)
    return l3

def diferencia(l1,l2):
    l3 = []
    for elem in l1:
        if not elem in l2:
            l3.append(elem)
    return l3
    
if __name__ == "__main__":
    l1 = [1,2,3,4,5,6,7,8,9]
    l2 = [1,3,5,7,9,11]
    l3 = interseccion(l1,l2)
    print l3
    l4 = union(l1,l2)
    print l4
    l5 = diferencia(l1, l2)
    print l5
    
    