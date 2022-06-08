import numpy as np

tolerancia = 0.1
def modulo(xk):
    elem = 0
    for i in range (1,len(xk)):
        elem += xk[i]**2
    elem = np.sqrt(elem)
    return elem 

def calcTol(xk, xk1):
    if ((modulo(xk)-modulo(xk1)) < tolerancia):
        return True
    else:
        return False

