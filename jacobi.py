from copy import copy
from tkinter.tix import Tree
import numpy as np

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
    for i in range (1,len(xk)+1):
        # print("elem = ", elem, " += xk[", i, "]^2 = ", xk[i] * xk[i])
        elem += xk[i] * xk[i]
    # print("elem = ", elem, " = sqrt(", elem, ")")
    elem = np.sqrt(elem)
    # print(elem)
    return elem 

def calcTol(xk, xkm1, tolerancia):
    return (abs(modulo(xk)-modulo(xkm1)) > tolerancia)

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
    met = int(input("[1] => Jacobi\n[2] => Gauss-Seidel\nElegir metodo a utilizar: "))
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
     
def vectorNulo(n):
    vecNulo = {1: 0}
    for i in range(1, n+1):
        vecNulo[i] = 0
    return vecNulo	
      
def calculoXKI(A, b, xk, xkm1, i, met):
    xk[i] = 0
    xk[i] += b[i]/A[i][i]
    for j in range(1, i):
        if met == 1:
            xk[i] -= (A[i][j]*xkm1[j]/A[i][i])
        else:
            xk[i] -= (A[i][j]*xk[j]/A[i][i])
    for j in range(i+1, len(A)+1):
        xk[i] -= (A[i][j]*xkm1[j]/A[i][i])
    return xk[i]
	
default = input('Desea usar el sistema por default? SI/NO = ')

if default == 'SI':
    print("Tamaño = 2")
    n = 2
    print("Matriz A:")
    A = {
		1: {
			1: 2,
			2: -1
		},
		2: {
			1: 1,
			2: 5
		}
	}
    print(A)
    print("Vector b:")
    b = {
		1: 3,
		2: 1
	}
    print(b)
    tol = 0.1
    print("Tolerancia = 0.1")    
    N = 30
    print("Número máximo de iteraciones = 30")      
    X0 = {
		1: 0,
		2: 0
	}
    print("Vector X0: ")
    print(X0)
    met = elegirMetodo()
else:
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
xk = vectorNulo(len(A))
xkm1 = copy(X0)

# Pruebo calculo de modulo

while k < N+1:
    for i in range(1, len(A)+1):
        xk[i] = calculoXKI(A, b, xk, xkm1, i, met)
    # if not calcTol(xk, xkm1, tol):
    #     print("Se llego al limite de tolerancia\nResultado:\n")
    #     break
    xkm1 = xk
    k+=1
print(xk)