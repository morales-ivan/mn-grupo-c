n = int(input("Tamanio = "))

A = {
    1: {1: 0}
}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        try:
            A[i]
        except:
            A[i] = {1: 0}
        A[i][j] = float(input("A[" + str(i) + "-" + str(j) + "]= "))