#any % 4 == 0 and (amy % 400> or any % 100 == 0)
def ano (a):
    if a%4==0 and (a%400>0 or a%100==0):
        print ("Es ano de traspaso")
    else:
        print ("No es ano de traspaso")

#PP
b=input("introduce un ano: ")
ano(int(b))
