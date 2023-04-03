def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
x = ["hola", "Adeu", "Si", "Matematics", "Alcaufar de Sant Roc", "Un senyor damunt un ruc, el ruc va caure"]
print("La paraula més llarga és: ", paraula_mes_gran(x))
