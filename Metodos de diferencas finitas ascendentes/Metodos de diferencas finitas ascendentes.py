# Os pontos a seguir relacionam a solubilidade P, do oleo mineral com a chuva em partes
# por milhoes (ppm), com a temperatura t, em graus centigrados. Utilizando interpolacao
# polinomial, o metodo de diferencas finitas ascendentes, estime o valor de t, considerando
# a solubilidade 200ppm, e os dados a seguir.

import matplotlib.pyplot as plt
import bisect
import sympy as sp

P = [136, 178, 220, 262] # Solubilidade  P em ppm 
t = [15, 50, 66, 76] # Temperatura t em celsius

x = 200

n = len(P)

Delta_t1 = []

# Calcula variação de y
for i in range(n-1):

    variacao = t[i+1]-t[i]

    Delta_t1.append(variacao) 

Delta_t2 = []

# Calcula variação de Delta_1
for i in range(n-2):

    variacao = Delta_t1[i+1]-Delta_t1[i]

    Delta_t2.append(variacao) 

# Calcula variação de Delta_3
Delta_t3 = Delta_t2[1]-Delta_t2[0]

#print(Delta_t1)
#print(Delta_t2)
#print(Delta_t3)

# Definindo a variável simbólica Z
Z = sp.Symbol('Z')

Polinomio = t[0]+Z*Delta_t1[0] + ((Z*(Z-1))/2)*Delta_t2[0] + ((Z*(Z-1)*(Z-2))/6)*Delta_t3 # Calcula o Polinomio

h = P[1]-P[0] # Calcula o espaçamento dos pontos

Z0 = (x-P[0])/h # Calcula Z0
#print("Z=", Z0)

estimativa = Polinomio.subs(Z, Z0) # Aplica o valor de Z na função Polinomio

#adiciona ponto descoberto nas listas 
posicao_insercao = bisect.bisect(P, x)# Encontrar a posição de inserção ordenada na lista de tempo
P.insert(posicao_insercao, x) # Inserir o ponto descoberto nas listas de forma ordenada 
t.insert(posicao_insercao, estimativa) # Inserir o ponto descoberto nas listas de forma ordenada 

#print(P)
#print(t)

print("\nP(x0+hz) = ", Polinomio)
print("\nQuando Z é igual a ", Z0, ", P(200) = ", round(estimativa, 2), "\n")# Imprimi com duas casa decimais

# Grafico Distância vs. Tempo
plt.title('Solubilidade x Temperatura')
plt.scatter(x, estimativa, color='red', label='Ponto Descoberto')# Adiciona o ponto descoberto ao gráfico
plt.plot(P, t)
plt.xlabel('Solubilidade(ppm)')
plt.ylabel('Temperatura(°C)')
plt.show()# Exibir o gráfico

