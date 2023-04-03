def llegir():
    l=[]
    a='a'
    while a!=".":
        a=input("Pon el nombre: ")
        if a!='.':
            l.append(a)
    return l

def ncp(l,c):
    p=[]
    x=0
    for e in l:
        if e[0]==c:
            x+=1
            p.append(e)
    print("El numero de palabras que comienzan {} són {} i són {}" .format(c,x,p))

#PP
o=llegir()
x=input("introduze el caracter qie desea buscar: ")
ncp(x,o)