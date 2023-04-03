def comptar_vocales():
    x=input("Introduce una palabra: ")
    a=0
    e1=0
    i1=0
    o=0
    u=0
    for e in x:
        if e=='a':
            a+=1
        if e=='e':
            e1+=1
        if e=='i':
            i1+=1
        if e=='o':
            o+=1
        if e=='u':
            u+=1
        print("{} tiene {} A, {} E, {} I, {} O, {} U".format(x,a,e1,i1,o,u))
