from math import floor, log, pow

def generador_de_primos(limite_alto):
	primos = []
	esPrimo = False
	j = 0
	
	primos.append(2)

	for i in range(3, limite_alto, 2):
		j = 0
		esPrimo = True
		while primos[j] * primos[j] <= i:
			if i % primos[j] == 0:
				esPrimo = False
				break;
			j += 1
		if esPrimo:
			primos.append(i)

	return primos


divisorMaximo = 20
p = generador_de_primos(divisorMaximo)
print p
resultado = 1

for i in range(0,len(p)):
	a = int(floor(log(divisorMaximo) / log(p[i])))
	print a
	resultado = resultado * int(pow(p[i],a))
	print resultado

print "El numero mas pequenioo que puede ser dividido entre el rango 1-20 es: %s" % (resultado)