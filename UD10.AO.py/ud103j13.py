# Funció que retorna la longitud
def longitut(a):
    count=0
    for i in a:
        count+=1
    return count
# Programa principal
b=[1,"a",[3,4],5,6]
print(longitut(b))
