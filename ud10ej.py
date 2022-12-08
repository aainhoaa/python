# Definició de funcions
def longitut(a):
    l = 0 
    for i in a:
        l +=1
    return l

# Aplicació principal
a = input("Introdueix una cadena: ")
b = longitut(a)
print ("La lomgitut", a, " és ", b)
c = list()
i="a"
while (i!='.'):
    x = input("Introdueix el següent element de la llista")
    c.append(x)
d = longitut(c)
print("La longitut", c, "és", d)
