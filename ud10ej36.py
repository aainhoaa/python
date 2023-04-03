def llegir_numero():
    return (int(input("Introdueixi un valor: ")))
def llegir_numero_float():
    return (float(input("Introdueixi un valor real: ")))
def calcular_prestec(q, i, a):
    return (q * (1+i/100)**a)

q=llegir_numero()
i=llegir_numero_float()
a=llegir_numero()
c=calcular_prestec(q, i, a)
print("Si sol·licita {} a un interés anual del {} pagaré {} euros".format (q, i, a, c))
