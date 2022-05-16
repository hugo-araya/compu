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
    print ("La funcion es : f(x) = ",str(a)+"x^2 + "+ str(b)+"x + "+str(c)+ " = 0")
    if a < 0:
        print ("La parabola es negativa")
    else:
        print ("La parabola es positiva")
    d = b*b - 4*a*c
    if d < 0:
        print ("La funcion no corta el eje x")
    else:
        if d == 0:
            x = -b/2*a
            print ("La Funcion se posa sobre el eje x en el punto: ("+str(x)+",0)")
        else:
            r = math.sqrt(d)
            x1 = (-b + r)/2*a
            x2 = (-b - r)/2*a
            print ("La funcion corta el eje x en los puntos")
            print ("("+str(x1)+",0)", "y en "+"("+str(x2)+",0)")
    print ("La funcion corta el eje y en : (0,"+str(c)+")")
    xv = -b/float(2*a)
    yv = (4*a*c -b*b)/float(4*a)
    print ("El vertice de la parabola se encuentra en ("+str(xv)+" , "+str(yv)+")")
    print (" ")
    print ("----------------------------------")
    print (" ")
    i = i +1
        
    
