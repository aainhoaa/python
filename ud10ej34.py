import random
def calculem_n_aleatoris():
    b=[]
    for i in range(4):
        b.append(random.randint(0,9))
    return b

def llegir_n_usuari():
    b=[]
    for i in range (4):
        b.append(int(input("Intro número")))
    return b

def comparar(a, b):
    totigual=0
    existeixen=0
    for i in range(4):
        if a [1]==b[i]:
            totigual+=1
        elif b[i] in a:
            existeixen+=1
    return totigual, existeixen

import random
a=calculem_n_aleatoris()
serfiv=0
while serfiv!=1:
    b=llegir_n_usuari()
    x,y=comparar(a,b)
    if x==4:
        print ("Has encertat tots els números {}".format(b))
    elif x<4 and y>0:
        print ("Has encertat {} números i n'hi ha {} que hi són però no són al seu lloc".format(x,y))
    elif x<4 and y==0:
        print("")
    elif x==0 and y>0:
        print("")

def comparar(a,b):
    a,b=0
    for i in range(4):
        if a [i]==b[i]:
            a+=1
        elif b[i]in a:
            b+=1
        else:
            c+=1
        if a==4:
            print("")
            return 1
        elif a>0 and y>0:
            print("")
            return 0
        elif a==0 and y>0:
            print("")
            return 0
        elif a>0 and y==0:
            print("")
            return 0
        else:
            print("")
            return 0

import random
a=calculem_n_aleatoris()
stop=0
while stop!=1:
    b=llegir_n_usuari()
    if comparar(a,b)==1:
        stop=1
    else:
        stop=0        
        