# Definició de funcions
def gran (x, y):
    a = x
    if(x>y):
        print(x, "és major que ", y)
    elif(y>x):
        print(y, "és menor que ", x)
        a = y
    else:
        print(x, "és igual que ", y)
    return a

# Aplicació principal
a = int(input("Escriure el primer valor: "))
b = int(input("Escriure el segon valor: "))
c = gran(a, b)
print("El major de ", a, "i", b, "és", c)
