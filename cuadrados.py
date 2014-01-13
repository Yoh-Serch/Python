suma_cuadrados = 0
suma_numeros = 0

for i in range(1,10001):
	suma_cuadrados += i**2
	suma_numeros += i

suma_numeros = suma_numeros**2

resta = suma_numeros - suma_cuadrados

print suma_numeros
print resta