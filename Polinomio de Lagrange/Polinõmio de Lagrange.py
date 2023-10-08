import matplotlib.pyplot as plt
import bisect

# Lista de dados
tempo = [0, 3, 5, 8, 13, 17] # Segundos
distancia = [0, 231, 335, 651, 993, 909] # Pés
velocidade = [63, 67, 72, 78, 72, 79] # pés/segundo

ponto_tempo = 10 #tempo a ser descoberto

n = len(tempo) # Ta

Sd  = 0
Sv = 0
 
for i in range(n):
    L = 1
    
    for j in range(n):
        if i != j: # Calcula polinômios de Lagrange L(x) caso i seja diferente de j
            L = L *((ponto_tempo - tempo[j])/(tempo[i]-tempo[j])) 

    # Calcula o polinômio interpolador de Lagrange
    Sd = Sd + distancia[i] *L # Calcula o valor da distância no t = 10s
    Sv = Sv + velocidade[i] *L # Calcula o valor da velocidade no t = 10s


#adiciona ponto descoberto nas listas 
posicao_insercao = bisect.bisect(tempo, ponto_tempo)# Encontrar a posição de inserção ordenada na lista de tempo
tempo.insert(posicao_insercao, ponto_tempo) # Inserir o ponto descoberto nas listas de forma ordenada
distancia.insert(posicao_insercao, Sd)
velocidade.insert(posicao_insercao, Sv)

print("\n")
print(tempo)
print(distancia)
print(velocidade)

# Grafico Distância vs. Tempo
plt.title('Distância x Tempo')
plt.scatter(ponto_tempo, Sd, color='red', label='Ponto Descoberto')# Adiciona o ponto descoberto ao gráfico
plt.plot(tempo, distancia)
plt.xlabel('Tempo(s)')
plt.ylabel('Distância(pé)')
plt.show()# Exibir o gráfico

# Gráfico Velocidade vs. tempo
plt.title('Velocidade x Tempo')
plt.scatter(ponto_tempo, Sv, color='red', label='Ponto Descoberto')# Adiciona o ponto descoberto ao gráfico
plt.plot(tempo, velocidade)
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade(pé por segundo)')
plt.show()# Exibir o gráfico

print("\nA estimativa da posição do carro e da sua velocidade quando t = 10s é respectivamente %.0f e %.0f.\n" %(Sd, Sv))