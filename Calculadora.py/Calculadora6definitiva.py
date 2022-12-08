# Funcions auxiliars
def menu_principal():
    print("""
    Menu Calculadora principal:
    1. Números enters
    2. Números reals
    3. Canvis de base
    0. Sortir
    """)
    opcio=input("Seleccioni l'opció que vulgui: ")
    return opcio

def menu_enters():
    print("""
            Menú Calculadora de números enters:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potència
            6. Mòdul
            7. Cocient
            0. Sortir
            """)
    opcio=input("Seleccioni l'opció que vulgui: ")
    return opcio

def menu_reals():
    print("""
            Menú Calculadora de números reals:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potència
            0. Sortir
            """)
    opcio=input("Seleccioni l'opció que vulgui: ")
    return opcio

def menu_canvis_de_base():
    print("""
            Menú Calculadora de canvis de base:
            1. Pasar de binari a decimal, octal i hexadecimal
            2. Pasar d'octal a binari, decimal i hexadecimal
            3. Pasar de decimal a binari, octal i hexadecimal
            4. Pasar d'hexadecimal a binari, octal i decimal
            0. Sortir
            """)
    opcio=input("Seleccioni l'opció que vulgui: ")
    return opcio

# Per a reduir el número de funcions farem de qualsevol número a decimal i d'aquí als altres
# Decimal a binari, octal i hexadecimal
def dectobin(numero):
    return bin(numero)
def dectooct(numero):
    return oct(numero)
def dectohex(numero):
    return hex(numero)
# Binari a octal, decimal i hexadecimal
def bintooct(numero):
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    a=int(numero,2)
    return a
def bintohex(numero):
    a=int(numero,2)
    return dectohex(a)
# Octal a binari, decimal i hexadecimal
def octtobin(numero):
    a = int(numero,8)
    return dectobin(a)
def octtodec(numero):
    a = int(numero,8)
    return a
def octtohex(numero):
    a=int(numero,8)
    return dectohex(a)
# Hexadecimal a binari, octal i decimal
def hextonum(hex): # Aquesta funció passa qualsevol hexadecimal a un numero
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor  = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum
        posicio += 1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a = int(hextodec2(numero))
    return a

# Progrma principal de la calculadora
opcio="1"
while(opcio!="0"):
    if (opcio!="0"):
        opcio = menu_principal()
    match opcio:
        case "1": # Calculadora de números enters
            opcio2=menu_enters()
            if (opcio2!="0"):
                a = int(input("Indiqui el primer operand: "))
                b = int(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ",c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menys ",b," és ",c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ",c)
                case "4":
                    c=a//b
                    print("La divisió de ",a," entre ",b," és ",c)
                case "5":
                    c= a ** b
                    print("La potència de ",a," elevat a ",b," és ",c)
                case "6":
                    c= a % b
                    print("El mòdul de ",a," mòdul ",b," és ",c)
                case "7":
                    c= a / b
                    print("El cocient de ",a," entre ",b," és ",c)
                case "0":
                    print("Adéu")
                    opcio="0"
                case other:
                    print("opció no vàlida!")
        case "2": # Calculadora de números reals
            opcio2=menu_reals()
            if (opcio2!="0"):
                a = float(input("Indiqui el primer operand: "))
                b = float(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=a+b
                    print("La suma de ",a," més ",b," és ", c)
                case "2":
                    c=a-b
                    print("La resta de ",a," menys ",b," és ", c)
                case "3":
                    c=a*b
                    print("La multiplicació de ",a," per ",b," és ", c)
                case "4":
                    c=a/b
                    print("La divisió de ",a," entre ",b," és ", c)
                case "5":
                    c= a ** int(b)
                    print("La potència de ",a," elevat a ",b," és ",c)
                case "0":
                    print("Adéu")
                    opcio="0"
                case other:
                    print("opció no vàlida!")
        case "3": # Canvis de base
            opcio2=menu_canvis_de_base()
            if (opcio2!="0"):
                a =input("Indiqui el número a convertir: ")
            match opcio2:
                case "1": # Binari a
                    b=bintooct(a)
                    c=bintodec(a)
                    d=bintohex(a)
                    print("El número binari ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "2": # Octal a
                    b=octtobin(a)
                    c=octtodec(a)
                    d=octtohex(a)
                    print("El número octal ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "3": # Decimal a
                    b=dectobin(int(a))
                    c=dectooct(int(a))
                    d=dectohex(int(a))
                    print("El número decimal ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
                case "4": # Hexadecimal a
                    b=hextobin(a)
                    c=hextooct(a)
                    d=hextodec(a)
                    print("El número hexadecimal ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
                case "0":
                    print("Adéu")
                    opcio="0"
                case other:
                    print("Opció no vàlida!")
        case "0":
            print("Adéu")
            opcio="0"
        case other:
            print("Adéu")
            opcio="0"
