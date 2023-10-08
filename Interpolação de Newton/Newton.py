#Um carro viajando em uma estrada reta é cronometrado em vários pontos. Os dados das observações são dados na tabela a seguir, 
#onde o tempo está em segundos, 
#a distância em pés e a velocidade em pés por segundo.

# Use a interpolaçao de Newton para fazer uma estimativa da posição do carro e da sua velocidade quando t = 15s.

import matplotlib.pyplot as plt
import bisect

def newton(x, y, valor):
    c = diferencasD(x, y)
    n = len(x)
    interpolacao = c[0]

    for i in range(1, n):
        a = c[i]
        for j in range(i):
            a *= (valor - x[j])
        interpolacao += a

    return interpolacao
def diferencasD(x, y):
    n = len(x)
    c= []
    for i in range(n):
        c.append(y[i])

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            c[i] = (c[i] - c[i-1]) / (x[i] - x[i-j])

    return c
    
y = [0, 231, 335, 651 ,993, 909]  #distancia
x = [0, 3, 5, 8, 13, 17]  #tempo
v = [63 , 67, 72, 78 , 72, 79] #velocidade 
interpolar = 15 # ponto buscado

resultadov = newton(x, v, interpolar)
resultado = newton(x, y, interpolar)

#adiciona ponto descoberto nas listas 
posicao_insercao = bisect.bisect(x, interpolar)# Encontrar a posição de inserção ordenada na lista de tempo
x.insert(posicao_insercao, interpolar) # Inserir o ponto descoberto nas listas de forma ordenada
y.insert(posicao_insercao, resultado)
v.insert(posicao_insercao, resultadov)

print("\nTempo=", interpolar, "\tVelocidade=", resultadov,"\tDistancia=", resultado, "\n")

# Grafico Distância vs. Tempo
plt.title('Distância x Tempo')
plt.scatter(interpolar ,resultado, color='red', label='Ponto Descoberto')# Adiciona o ponto descoberto ao gráfico
plt.plot(x, y)
plt.xlabel('Tempo(s)')
plt.ylabel('Distância(pé)')
plt.show()# Exibir o gráfico


# Gráfico Velocidade vs. tempo
plt.title('Velocidade x Tempo')
plt.scatter(interpolar, resultadov, color='red', label='Ponto Descoberto')# Adiciona o ponto descoberto ao gráfico
plt.plot(x, v)
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade(pé por segundo)')
plt.show()# Exibir o gráfico
