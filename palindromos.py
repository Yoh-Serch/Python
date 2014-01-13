def es_palindromo(numero):
	numero_inverso = ""
	for i in range(len(numero)-1,-1,-1):
		numero_inverso += numero[i]
	if numero == numero_inverso:
		return True
	else:
		return False


for i in range(900,1000):
	for j in range(900,1000):
		numero = i * j
		numero_string = str(numero)
		if es_palindromo(numero_string):
			print numero


