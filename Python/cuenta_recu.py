#Importamos el modulo sys para ver y modificar parametros del sistema
import sys
 
#Definimos una funcion recursiva que se llama a si misma
def funcion(param):
 
  if param < sys.getrecursionlimit()-2:
    param+=1
    funcion(param)
    print (param)
 
  return param
 
if __name__ == "__main__":
 
  #Mostramos el limite de recursividad actual
  print (sys.getrecursionlimit())
  #Lo modificamos a 30
  sys.setrecursionlimit(30)
 
  #Llamamos a la funcion que hemos definido.
  print ("El resultado de la funcion es "+str(funcion(0)))