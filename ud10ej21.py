def menu():
    print("""
    Menu:
        1. Dibuix un
        2. Dibuix dos
        0. Sortir
    """)
    opcio=input("Seleccioni el dibuix que vulgui: ")
    return opcio

def crear_punts(a):
    match a:
        case "1":
            print("""
               ...    ...
              .    . .   .
             .      .     .
             .            .
              .          .
               .        .
                .      .
                 .    .
                  .  .
                   ..
              """)
        case "2":
            print(""" 
            _____
            |   |
            |___|
             """)
        case other:
            print("Adéu")

opcio=2
while(opcio!=0):
    opcio = menu ()
    crear_punts(opcio)
print("Adéu. ja hem acabat")
