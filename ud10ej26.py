def bintodec (bin):
    return int(bin,2)
def llbintodec(llbin):
    lldec = []
    for e in llbin:
        lldec.append(bintodec(e))
    return lldec
#Programa principal
a = ["111", "11", "1010","1000"]
b = llbintodec(a)
for i, e in enumerate(b):
    print("El número binari : ", a[i], " es correspon amb el número decimal: ", e)
