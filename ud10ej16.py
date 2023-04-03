def invertir(a):
    b=list(a)
    c=b[::-1]
    r="".join(c)
    return r

#Programa Principal
b=input("Itrodueix una paraula")
c=invertir(b)
print("La paraula", b, "Si la girem és", c)
