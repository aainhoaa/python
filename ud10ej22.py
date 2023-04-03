def gran_llista(a):
	a.sort()
	return a[::-1]

# Programa principal
a = [3, 40, 34, 15, 4, 5, 7, 9]
c = gran_llista(a)
print(c[0])
