def palindromo(texto):
	""" 
	elimina caracteres no deseados, compara el texto orignal con el volteado
	"""
	texto = texto.lower()
	texto = texto.replace(" ", "")
	if str(texto) == str(texto)[::-1]:
	        print ("Es palindromo")
	else:
		print ("No es")

def main():
	"""
	ciclo infinito hasta que el usuario quiera cerrar el programa
	"""	
	while True:
    		texto = raw_input("Ingrese su palabra ")
    		palindromo(texto)
    		flag = raw_input("Desea ingresar otra palabra? S/N ")
		if flag == "N":
			break

main()
