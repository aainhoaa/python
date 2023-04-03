# Per a treballar amb dates: https://codigofacilito.com/articulos/fechas-python
# Per a treballar amb taules: https://www.delftstack.com/es/howto/python/data-in-table-format-python/

from datetime import date
from datetime import datetime

def GetNames(aactual):
	a = []
	print("Introdueixi els nom i la data de naixament de les 4 persones:")
	for i in range(0,4):
		v = [0,0,0]
		v[0] = input("Escriu el nom de la {}a persona: ".format(i+1))
		v[1] = input("Escriu l'any de naixament de {}: ".format(v[0]))
		v[2] = int(aactual) - int(v[1])
		a.append(v)
	return a

#Programa Principal
avui = date.today()
aactual = avui.year
x = GetNames(aactual)
print("L'any actual és: ", aactual)
print ("{:<20} {:<20} {:<20}".format('Nom','Data naixament','Anys que farà aquest any'))
for e in x:
	print("{:<20} {:<20} {:<20}".format(e[0], e[1], e[2]))
