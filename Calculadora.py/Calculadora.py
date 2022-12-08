print("menú")
print("1. Sumar \n")
print("2. Restar \n")
print("3. Multiplicar \n")
print("4. Dividir \n")
print("0. Sortir \n")
opcio=input("Seleccioni l'opció que vulgui: ")
a = input("Indiqui el primer operand: ")
b = input("Indiqui el segon operand: ")
match opcio:
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," més ",b," és ",c)
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menys ",b," és ",c)
    case "3":
        c=int(a)* int(b)
        print("La multiplicació de ",a," por ",b," és ",c)
    case "4":
        c=int(a)/ int(b)
        print("La rdivició de ",a," per ",b," és ",c)
    case "0":
        print("Adéu")
    case other:
        print("opció no válida!")
        