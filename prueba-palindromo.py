def palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    if str(texto) == str(texto)[::-1]:
        print ("es palindromo")
    else:
        print ("no es")

