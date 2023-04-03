def llegir():
    llista=[]
    a='a'
    while a!='.':
        a=input("Introdueix un nombre: ")
        if a!='.':
            llista.append(int(a))
    return tuple(llista)

# 2n. Funció pròpiament dita
def mostrar_majors_que(a, num):
    for e in a:
        if e > num:
            print(e)

# 3r. Programa principal (PP)
x=llegir()
i=input("Introdueix el número que vol comprar: ")
mostrar_majors_que(x,int(i))
