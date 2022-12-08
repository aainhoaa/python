# Definició de funcions
def gran_de_tres (x,y,z):
    a=x
    if(x>y):   # x>y
        if(x>z):   # x>y and x>z
            a = x
        elif (z>x):   # x>y and z > x => z és el major
            a = z
        else:   # Aqui x = z > y => x,z són els majors
            a = x 
    elif (y>x):   # y>x
        if (y>z):   # y>x and y>z => y és el major
            a = y
        elif (z>y):   # y>x and z>y => z és el major
            a = z
        else:   # Aqui y > x and z=y ==> z,y són els majors
            a = y
    else:   # x=y
        if (x>z):   # x=y and x>z ==> x,y són els majors
            a = x
        elif (z>x):   # x=y and z>x ==> z és el major
            a = z
        else:   # x=y=z ==> x,y,z són iguals
            a = x
    return a 

# Aplicació principal
a = int(input("Escriure el primer valor: "))
b = int(input("Escriure el segon valor: "))
c = int(input("Escriure el tercer valor: "))
d = gran_de_tres(a,b,c)
print("El major de ", a, ", ",b, ", ",c," és ", d)
