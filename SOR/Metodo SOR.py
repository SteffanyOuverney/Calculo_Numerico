#Dado o sistema linear abaixo, com ε ≤ 10−15, e x0 = (0, 0, 0).

#Declaração das constantes do sistema linear
A = ([[5.0,3.0,-2.0,1.0],
      [1.0,-4.0,2.0,3.0],
      [1.0,2.0,-3.0,1.0],
      [2.0,1.0,-2.0,3.0]])

#Declaração do vetor resultado do sistema
B = [-6.0,10.0,-10.0,-7.0]

#Declaração do vetor x inicial
x = [0.0, 0.0, 0.0, 0.0]

#fator de relaxação
w = 1.02

#tolêrancia
tol = 10**(-15)

iter = 0

max_intera = 53

#loop enquanto iter for menor que max_intera ou vetor x atual - vetor anterior for menor que tolêrancia
while iter < max_intera:
    #percorre a  linha da matriz
    for i in range(len(A)):
        xo = x.copy() #faz uma copia de x para xo
        soma_anterior = 0
        #percorre a  coluna da matriz
        for j in range(len(A)):
            if j != i:
                soma_anterior += A[i][j] * x[j]
            #calcula o resíduo
            Residuo = B[i] - soma_anterior - (A[i][j]*xo[j])
            #print("Residuo:", Residuo)
            #print("\n")

            #calcula o valor do novo x
            x[i] = (1 - w) * xo[i] + w*(Residuo/A[i][i])

    #subtrai x atual - vetor anterior
    for i  in range (len(x)):
        parada = abs(x[i] - xo[i]) 
    
    #verifica se parada é menor que tol
    if (parada < tol):
        break

    #printa a iteração
    print("Iteration:", iter)
    #printa o valor do vetor x a cada iteração
    print("x:", x)
    print("\n")

    iter += 1

#printa a solução do sistema bem como o número  de iterações 
print("Solução do sitema: ", x)
print("\n")
print("Número de iterações: ", iter)
print("\n")