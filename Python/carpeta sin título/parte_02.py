
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

def obtener_dominios(correos):
	dominios = []
	for correo in correos:
		posicion = correo.rfind("@")
		dominios.append(correo[posicion+1:])
	return dominios

if __name__ == "__main__":
	correos = lee_correos()
	dominios = obtener_dominios(correos)
	print dominios