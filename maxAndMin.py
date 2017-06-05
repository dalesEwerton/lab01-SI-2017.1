#coding: utf: -8

def maximo(numeros):

	max = numeros[0]

	for i in range(len(numeros) -1):
		if(max < numeros[i+1]):
			max = numeros[i+1]

	return max

