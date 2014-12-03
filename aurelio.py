
def cinco_impares(inicio):
    cont = 0
    valor = inicio
    while  cont < 5:
        if valor % 2 != 0:
            cont += 1
            print valor 
        valor += 1 

cinco_impares(5)
print "------"
cinco_impares(8)
