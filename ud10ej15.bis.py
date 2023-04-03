# funcio sumar elements de la llista
def sumar_llista(a):
    sumatori=0
    for i in a:
        sumatori = sumatori + (i*i) # sumatori +=(i*i)
    return sumatori
# Funció multiplicar elelements de la llista
def multiplicar_lista(a):
    multiplicacio=1
    for i in a:
        multiplicacio *= i
    return multiplicacio

# Programa principal
h = [1, 3, 4, 6, 7, 8, 15, 17]
print("La suma dels elements de la llista és: ", sumar_llista(h))
print("La multiplicació dels elements de la llista és: ", multiplicar_lista(h))
