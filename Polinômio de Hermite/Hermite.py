#Um carro viajando em uma estrada reta é cronometrado em vários pontos. Os dados das observações são dados na tabela a seguir, 
#onde o tempo está em segundos, 
#a distância em pés e a velocidade em pés por segundo.

# Use a derivada do polinômio de Hermite para determinar se o carro excedeu alguma vez o limite de velocidade de 55milhas/h na estrada. 
# Em caso afirmativo, qual foi a primeira vez em que o carro excedeu essa velocidade?

def hermite_derivative(x, y, dy, t):
    # Calcula a derivada de Hermite no ponto t 
    n = len(x)
    result = 0.0

    for i in range(n):
        term = dy[i]
        for j in range(n):
            if i != j:
                term *= (t - x[j]) / (x[i] - x[j])
        result += term

    return result

# Dados fornecidos
distancia = [0, 231, 335, 651, 993, 909]
tempo = [0, 3, 5, 8, 13, 17]
velocidade = [63, 67, 72, 78, 72, 79]

# Ajuste de Hermite aos dados de tempo e velocidade
n = len(tempo)
x = tempo
y = velocidade

dy = [hermite_derivative(tempo, velocidade, [1] * n, t) for t in tempo]

# Encontrar o instante em que a velocidade passa de 80
instante = None

limite_de_velocidade = (55*1.46667) # Convertendo para pés po segundo

for i in range(n - 1):

    if y[i] <= limite_de_velocidade and y[i + 1] > limite_de_velocidade:
        t = x[i] + (x[i + 1] - x[i]) * (limite_de_velocidade - y[i]) / (y[i + 1] - y[i])
        instante = t
        break

if instante is not None:
    print(("\nInstante em que a velocidade passa de"), limite_de_velocidade, (":") , instante, ("\n"))
else:
    print(("\nA velocidade não ultrapassa "), limite_de_velocidade, ("."), ("\n"))