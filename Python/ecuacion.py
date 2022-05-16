import math
import random
i = 0
print (" ")
print ("----------------------------------")
print (" ")
while i <10:
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100) 
    print ("La ecuacion es : ",str(a)+"x^2 +"+ str(b)+"x + "+str(c)+ " = 0")
    d = b*b - 4*a*c
    if d < 0:
        print ("La ecuacion no tiene solucion en los reales")
    else:
        if d == 0:
            x = -b/2*a
            print ("x = ", x)
        else:
            r = math.sqrt(d)
            x1 = (-b + r)/2*a
            x2 = (-b - r)/2*a
            print ("x1 = ", x1)
            print ("x2 = ", x2)
    print (" ")
    print ("----------------------------------")
    print (" ")
    i = i +1
        
    
