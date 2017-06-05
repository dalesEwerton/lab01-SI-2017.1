#coding: utf: -8

def maximo(numeros):

	max = numeros[0]

	for i in range(len(numeros) -1):
		if(max < numeros[i+1]):
			max = numeros[i+1]

	return max


def minimo(numeros):

	min = numeros[0]

	for i in range(len(numeros) -1):
		if(min > numeros[i+1]):
			min = numeros[i+1]

	return min

