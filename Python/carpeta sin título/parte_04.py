
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

def elimina_repetidos(dominios):
	nueva = []
	for elemento in dominios:
		if not elemento in nueva:
			nueva.append(elemento)
	return nueva

def elimina_genericos(dominios):
	genericos = ['com', 'gov' ,'edu' ,'org' ,'net' ,'mil']
	dominios_sin_repetidos = []
	for dominio in dominios:
		tld = dominio[len(dominio)-3:]
		if not tld in genericos:
			dominios_sin_repetidos.append(dominio)
	return dominios_sin_repetidos

def todos_los_dominios(correos):
	dominios = []
	for correo in correos:
		posicion = correo.rfind("@")
		dominios.append(correo[posicion+1:])	
	return dominios

def obtener_dominios(correos):
	dominios = todos_los_dominios(correos)
	dominios = elimina_repetidos(dominios)
	# dominios = list(set(dominios))
	dominios = elimina_genericos(dominios)
	dominios.sort()
	return dominios

def contar_tld(correos):
	dominios = todos_los_dominios(correos)
	dominios = elimina_genericos(dominios)
	tlds = []
	lista_tld = []
	for dominio in dominios:
		tld = dominio[len(dominio)-2:]
		tlds.append(tld)
	tlds_a_contar = list(set(tlds))
	for t in tlds_a_contar:
		contar = tlds.count(t)
		lista_tld.append([t, contar])
	return lista_tld

if __name__ == "__main__":
	correos = lee_correos()
	dominios_sin_repetidos = obtener_dominios(correos)
	print dominios_sin_repetidos
	tlds = contar_tld(correos)
	print tlds
