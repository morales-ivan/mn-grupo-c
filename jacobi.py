def cargoMatriz(n):
	matriz = []

	print("Ingrese los valores de la matriz A: \n")
	for i in range(0, n):
		fila = []

		print("Insertando los elementos de la fila " + str(i + 1) + "")

		for j in range(0, n):
			fila.append(float(input("Ingrese el elemento " + str(j + 1) +
                           " (A[" + str(i + 1) + "][" + str(j + 1) + "]): ")))

		matriz.append(fila)
		print("")

	return matriz


n = input("Tamanio = ")
prueba = cargoMatriz(n)
