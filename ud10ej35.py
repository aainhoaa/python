def llegir_paraula():
    return(input("Introdueixi una paraula"))

def comparar_paraules(a,b):
    if a==b:
        print("Són iguals per tant segur que rimen")
    elif a[-3:]==b[-3:]:
        print("Rimen perque les 3 darreres lletres són iguals")
    elif a[-2:]==b[-2:]:
        print("Rimen un poc perque només coincideixen les 2 darreres lletres")
    elif a[-1:]==b[-1:]:
        print("Rimen molt poc perque només la ultima lletra rima")
    else:
        print("No rimen")
        