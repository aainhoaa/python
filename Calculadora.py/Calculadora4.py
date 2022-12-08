# Funcions auxiliars
def menu_principal():
    print("""
    Calculadora
    Menu:
    1. Numeros enteros
    2. Numeros reales
    3. Canvis de base
    0. Sortir
    """)
    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_enters():
    print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            6. Modul
            7. Cociente
            0. Sortir
            """)
    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_reals():
    print("""
            Menu Calculadora de nuemros enteros
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            0. Sortir
            """)
    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio 

def menu_canvis_de_base():
    print("""
            Menu Calculadora de cambios de base
            1. Pasar de decimal a binario, octal y hexadecimal
            2. Pasar de Binario a decimal, octal y hexadecimal
            3. Pasar de Octal a binario, decimal y hexadecimal
            4. Pasar de Hexadecimal a Binario, Octal y Decimal
            0. Sortir
            """)
    opcio=input("Selecciona l'opcio que vulgui: ")
    return opcio

#Funcions menu 3 cambios de base
# Bin a octal
def bintooct(nbin):
    octaldigit = 0
    octalnum = []
    i = 0
    mul = 1
    chk = 1
    while nbin!=0:
        rem = nbin % 10
        octaldigit = octaldigit + (rem * mul)
        if chk%3==0:
            octalnum.insert(i, octaldigit)
            mul = 1
            octaldigit = 0
            chk = 1
            i = i+1
        else:
            mul = mul*2
            chk = chk+1
        nbin = int(nbin / 10)
    if chk!=1:
        octalnum.insert(i, octaldigit)
    return octalnum

def bintodec(nbin):
    ndec = 0 
    for posicion, digito_string in enumerate(nbin[::-1]):
        ndec += int(digito_string) * 2 ** posicion
    return ndec

def bintohex(nbin):
    bnum = int(nbin)
    temp = 0
    mul = 1
    # counter to check group of 4
    count = 1
    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
    # counter for hexadecimal number array
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
        # check if group of 4 completed
        if count % 4 == 0:
            # check if temp < 10
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
        # group of 4 is not completed
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
    # check if at end the group of 4 is not
    # completed
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
    # check at end the group of 4 is completed
    if count == 1:
        i = i-1
    return hexaDeciNum
  

# Octal a binari
def octtobin(noct):
    rev = 0
    chk = 0
    while noct!=0:
        rem = noct%10
        if rem>7:
            chk = 1
            break
        rev = rem + (rev*10)
        noct = int(noct/10)
    if chk == 0:
        noct = rev
        binnum = ""
        while noct!=0:
            rem = noct%10
            if rem==0:
                binnum = binnum + "000"
            elif rem==1:
                binnum = binnum + "001"
            elif rem==2:
                binnum = binnum + "010"
            elif rem==3:
                binnum = binnum + "011"
            elif rem==4:
                binnum = binnum + "100"
            elif rem==5:
                binnum = binnum + "101"
            elif rem==6:
                binnum = binnum + "110"
            elif rem==7:
                binnum = binnum + "111"
            noct = int(noct/10)
    return binnum
def octtodec(noct):
    decimal = 0
    posicion = 0
    # Invertir octal, porque debemos recorrerlo de derecha a izquierda
    # pero for in empieza de izquierda a derecha
    noct = noct[::-1]
    for digito in noct:
        valor_entero = int(digito)
        numero_elevado = int(8 ** posicion)
        equivalencia = int(numero_elevado * valor_entero)
        decimal += equivalencia
        posicion += 1
    return decimal
def octtohex(noct):
    chk = 0
    i = 0
    decnum = 0
    while noct!=0:
        rem = noct%10
        if rem>7:
            chk = 1
            break
        decnum = decnum + (rem * (8 ** i))
        i = i+1
        noct = int(noct/10)
    if chk == 0:
        i = 0
        hexdecnum = []
        while decnum != 0:
            rem = decnum % 16
            if rem < 10:
                rem = rem + 48
            else:
                rem = rem + 55
            rem = chr(rem)
            hexdecnum.insert(i, rem)
            i = i + 1
            decnum = int(decnum / 16)
    return hexdecnum

#Decimal a binari
def dectobin(numero_decimal):
    numero_binario = 0
    multiplicador = 1
    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10
    return numero_binario

def dectooctal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def dectohex(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal

#Hexadecimal a ...

def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)
def hextobin(nhex):
    ini_string = "1a"
    print ("Initial string", ini_string) 
    res = "{0:08b}".format(int(ini_string, 16)) 
    return res
def hextooct(nhex):
    chk = 0
    decnum = 0
    hexdecnumlen = len(nhex)
    hexdecnumlen = hexdecnumlen-1
    i = 0
    while hexdecnumlen>=0:
        rem = nhex[hexdecnumlen]
        if rem>='0' and rem<='9':
            rem = int(rem)
        elif rem>='A' and rem<='F':
            rem = ord(rem)
            rem = rem-55
        elif rem>='a' and rem<='f':
            rem = ord(rem)
            rem = rem-87
        else:
            chk = 1
            break
        decnum = decnum + (rem * (16 ** i))
        hexdecnumlen = hexdecnumlen-1
        i = i+1
    if chk==0:
        i = 0
        noct = []
        while decnum!=0:
            rem = decnum%8
            noct.insert(i, rem)
            i = i+1
            decnum = int(decnum/8)

    return noct

def hextodec(nhex):
    # Convertir a minúsculas para hacer las cosas más simples
    nhex = nhex.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    nhex = nhex[::-1]
    decimal = 0
    posicion = 0
    for digito in nhex:
        print(f"Decimal es {decimal}")
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        print(f"El verdadero valor de {digito} es {valor}")
        elevado = 16 ** posicion
        print(
            f"Elevamos 16 a la potencia {posicion}, el resultado es {elevado}")
        equivalencia = elevado * valor
        print(
            f"Multiplicamos el número elevado por el valor del carácter actual: {equivalencia}")
        decimal += equivalencia
        print(f"Ahora decimal es {decimal}")
        posicion += 1
    return decimal

# Progrma principal de la calculadora
opcio=1
while(opcio!=0):
    opcio= menu_principal()
    match opcio:
        case "1": # Calculadora de números enters
            opcio2=menu_enters()
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=int(a)+int(b) 
                    print("La suma de ",a," mes ",b," es ",c)
                case "2":
                    c=int(a)-int(b)
                    print("La resta de ",a," menys ",b," es ",c)
                case "3": 
                    c=int(a)*int(b)
                    print("La multiplicacio de ",a," per ",b," es ",c)
                case "4": 
                    c=int(a)/int(b)
                    print("La divisio de ",a," entre ",b," es ",c)
                case "5":
                    c= (a) ** (b)
                    print("La potencia de ",a," elevat a ",b," es ",c)
                case "6":
                    c= (a) % (b)
                    print("El modul de ",a," mòdul ",b," és ",c)
                case "7":
                    c= (a) // (b)
                    print("El cociente de ",a," entre ",b," es ",c)
                case "0": 
                    print("Adeu")
                    opcio=0
                case other:
                    print("opcion no valida")
        case "2": # Calculadora de números reals
            opcio2=menu_reals()
            a = float(input("Indiqui el primer operand: "))
            b = float(input("Indiqui el segon operand: "))
            match opcio2:
                case "1":
                    c=float(a)+float(b) 
                    print("La suma de ",a," mes ",b," es ", c)
                case "2":
                    c=float(a)-float(b)
                    print("La resta de ",a," menys ",b," es ", c)
                case "3": 
                    c=float(a)*float(b)
                    print("La multiplicacio de ",a," per ",b," es ", c)
                case "4": 
                    c=float(a)/float(b)
                    print("La divisio de ",a," entre ",b," es ", c)
                case "5":
                    c= float(a) ** int(b)
                    print("La potencia de ",a," elevado a ",b," es ",c)
                case "0": 
                    print("Adeu")
                    opcio=0
                case other:
                    print("opcion no valida")
        case "3": # Canvis de base
            opcio2=menu_canvis_de_base()
            a =input("Indiqui el nuombre: ")
            match opcio2:
                case "1": # Binari a
                    b=bintooct(int(a))
                    c=bintodec(int(a))
                    d=bintohex(int(a))
                    print("El número ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "2": # Octal a
                    b=octtobin(int(a))
                    c=octtodec(int(a))
                    d=octtohex(int(a))
                    print("El número ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
                case "3": # Decimal a
                    b=dectobin(int(a))
                    c=dectooctal(int(a))
                    d=dectohex(int(a))
                    print("El número ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
                case "4": # Hexadecimal a
                    b=hextobin(int(a))
                    c=hextooct(int(a))
                    d=hextodec(int(a))
                    print("El número ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
                case "0":
                    print("Adéu")
                    opcio=0
                case other:
                    print("Opció no vàlida!")
        case "0":
            print("Adéu")
