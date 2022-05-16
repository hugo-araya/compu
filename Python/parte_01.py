
def lee_correos():
	correos = []
	archivo = open("correos.txt")
	lineas = archivo.readlines()
	for linea in lineas:
		if linea[-1] == "\n":
			# linea = linea.rstrip("\n")
			linea = linea[:-1]
		correos.append(linea)
	archivo.close()
	return correos

if __name__ == "__main__":
	correos = lee_correos()
	print (correos)