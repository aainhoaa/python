def filtrar_paraules(a, num):
    b = list()
    for e in a:
        if num < len(e):
            b.append(e)
    return b

x = ["Hola", "Sí", "un senyor damuny un ruc"]
a = input ("Indicar la longitud de les paraules que vols filtrar: ")
y = filtrar_paraules(x,int(a))
print("Les paraules de igual o més tamany de ", a, " són: ", y)
