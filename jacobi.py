from tkinter.tix import Tree
import numpy as np

def printMatriz(d, space=5, fill='0'):
    strs = ' '.join('{{{0}:^{1}}}'.format(str(p), str(space)) for p in range(len(d) + 1))
    std = sorted(d)
    print(strs.format(" ", *std))
    for x in std:
        print(strs.format(x, *(d[x].get(y, fill) for y in std)))

def cargarMatriz(nombre, n):
	matriz = {
		1: {1: 0}
	}
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			try:
				matriz[i]
			except:
				matriz[i] = {1: 0}
			matriz[i][j] = float(input(nombre + "[" + str(i) + "-" + str(j) + "]= "))
	return matriz

def modulo(xk):
    elem = 0
    for i in range (1,len(xk)):
        elem += xk[i]**2
    elem = np.sqrt(elem)
    return elem 

def calcTol(xk, xkm1, tolerancia):
    return ((modulo(xk)-modulo(xkm1)) < tolerancia)

def cargarColumna(nombre, n):
	col = {
		1: 0
	}
	for i in range(1, n + 1):
		try:
			col[i]
		except:
			col[i] = 0
		col[i] = float(input(nombre + "[" + str(i) + "]= "))


def esMatrizDominante(matriz):
	tamanio = len(matriz)
	for i in range(1, tamanio+1):
		valorDiagonal = abs(matriz[i][i])
		suma = 0
		for j in range(1, tamanio+1):
			if i == j:
				continue
			suma += abs(matriz[i][j])
		if(suma >= valorDiagonal):
			return False
	return True


def elegirMetodo():
    met = int(input("[1] => Jacobi\n[2] => Gauss-Seidel\nElegir metodo a ultilizar: "))
    while met != 1 and met != 2:
        met = int(input(print("Ingrese un numero de metodo valido: ")))
    return met

def matrizNula(n):
    matNula = {1: {1: 0}}
    for i in range(1, n+1):
        for j in range(1, n+1):
            try:
                matNula[i]
            except:
                matNula[i] = {1: 0}
            matNula[i][j] = 0
    return matNula	
     
n = int(input("Tamanio = "))
A = cargarMatriz("A", n)

if not esMatrizDominante(A):
	print("A no es matriz diagonal estrictamente dominante")
	exit()
 
b = cargarColumna("b", n)
tol = float(input("Tolerancia = "))

if tol < 0.0000001:
	print("La tolerancia es muy pequeña")
	exit()
 
if tol > 1:
	print("La tolerancia es muy grande (>1)")
	exit()

N = int(input("Numero maximo de Iteraciones = "))

if N > 10000:
	print("El numero de iteraciones es mas que 10000")
	exit()

X0 = cargarColumna("X0", n)

met = elegirMetodo()

k = 1
xk = matrizNula(n)
xkm1 = X0
for k in range(1, N+1):
 	for i in range(1, N+1):
		xk = calculoXK(A, b, i, met)
 	if not calcTol(xk, xkm1):
    	print("Se llego al limite de tolerancia\nResultado:\n")
		printMatriz(xk)
	else:
		xkm1 = xk