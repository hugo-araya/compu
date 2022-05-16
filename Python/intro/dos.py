# Real Nota1, Nota2, Nota3
# Real Promedio
#String Mensaje
Nota1 = input("Nota 1: ")
Nota2 = input("Nota 2: ")
Nota3 = input("Nota 3: ")
Promedio = (Nota1 + Nota2 + Nota3) / 3
if Promedio >= 4.0:
	Mensaje = "Alumno Aprobado"
else:
	Mensaje =  "Alumno Reprobado"
print Mensaje
