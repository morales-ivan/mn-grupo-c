def cargaMatriz(n):
	matriz = {
		1: {1: 0}
	}
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			try:
				matriz[i]
			except:
				matriz[i] = {1: 0}
			matriz[i][j] = float(input("A[" + str(i) + "-" + str(j) + "]= "))
	return matriz

def cargarColumna(n):
	col = {
		1: 0
	}

	for i in range(1, n + 1):
		try:
			col[i]
		except:
			col[i] = 0
		col[i] = float(input("b[" + str(i) + "]= "))


def esMatrizDominante(matriz):
	tamanio = len(matriz)
	for i in range(1, tamanio+1):
		valorDiagonal = abs(matriz[i][i])
		suma = 0
		for j in range(1, tamanio+1):
			if i == j:
				continue
			suma += abs(matriz[i][j])
		if(suma <= valorDiagonal):
			return False
	return True


n = int(input("Tamanio = "))
A = cargaMatriz(n)
b = cargarColumna(n)
