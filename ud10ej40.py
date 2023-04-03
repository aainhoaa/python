def llegir_numeros():
    return(int(input("")))
def taula_multiplicar(a):
    for i in range(20):
        print ("{} x {}".format(i, a, i*a))

a=llegir_numeros()
taula_multiplicar(a)
