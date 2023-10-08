import numpy as np

#cria um array a partir de uma sequência de elementos
A = np.array([[1.94, 2.87, 4.33, -2.96],
              [1.48, 1.48, 2.80, 2.52],
              [6.31, 2.01, 1.98, 1.65],
              [8.27, 4.39, 1.64, 3.98]])

B = np.array([[2.30], [4.88], [9.67], [3.73]])

A_copia = np.copy(A) #Faz uma copia da Matriz A

# Formatar as casas decimais e evitar a notação científica
np.set_printoptions(precision=10, suppress=True)


def decomposicao_lu(A):
    n = len(A) # obtem o número de linhas do array (como A é uma matriz quadrada n é o número de linhas e colunas)
    L = np.eye(n, n)  # Cria uma A identidade n x n
    U = np.zeros((n, n))  # Cria uma A de zeros n x n

    passos = 0 # conta os passos da decomposição
    
    print("\nValores do calculo de cada linha [ L_n-multipliadorL_n*L_pivo]")

    for i in range(n-1):
        # Calcula os elementos da matriz L e U
        pivo = A[i, i]
        for k in range(i+1, n):
            multiplicador = A[k, i] / pivo  # calcula o multiplicador
            L[k, i] = multiplicador  # armazena na matriz L os multiplicadores 
            A[k, :] = A[k, :] - multiplicador * A[i, :]
            print("\nMatriz A[", i ,"]:")
            print(A)
            passos += 1

    U = A  # a matriz A modificada é a matriz U

    return L, U, passos

L, U, passos = decomposicao_lu(A)

def LY_B(L, B): #calcula L.Y = B

   Y = np.linalg.solve(L,B) #retorna a solução do sistema de equação linear

   return Y

Y = LY_B(L, B)

def UX_Y(U, Y): #calcula U.X = Y

   X = np.linalg.solve(U, Y) #retorna a solução do sistema de equação linear

   return X

X = UX_Y(U, Y)

#verifica se o vetor X é a solução
Verificar = np.dot(A_copia, X)

#verifica se  A = L*U
A_verificado = np.dot(L, U)

#printa os dados
print("\nNúmero de passos: ", passos)

print("\nVetor permutação B: \n", B)

print("\nMatriz L: \n", L)

print("\nMatriz U: \n", U)

print('\nCalculando L.Y = B\n')
print("Y = \n", Y)

print("\nCalculando a solução da matriz U.X = Y\n")
print("X = \n", X)

print("\nVerificando se o vetor X são as raizes:  \n", Verificar)

print("\nVerificando se A = LU\n", A_verificado)
print("\n")