# Uma hidreletrica tem capacidade maxima de 60MW, que e determinada por tres geradores de 30MW, 15MW e 15MW, respectivamente. A demanda de energia varia,
# num ciclo de 24 horas, sendo que a demanda minima ocorre entre 5h e 8h, e a maxima
# entre 13h e 16h. Utilizando interpolacao polinomial, e os metodos de diferencasdividas
# e finitas ascendentes, estime a demanda minima e a maxima, e o horario em que cada
# uma ocorre, considerando os dados a seguir. Faca as tabelas das demandas minimas e
# maximas dos turnos manha e tarde.

import numpy as np

horariosTarde = [13, 14, 15, 16]
demandasTarde = [36.50, 43.00, 34.00, 31.20]

horariosManhã = [5, 6, 7, 8]
demandasManhã = [16.40, 15.20, 14.90, 16.00]

# diferenças divididas
def diferenca_dividida(x, y):
    n = len(x)
    t = np.zeros((n, n))
    t[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            t[i][j] = (t[i + 1][j - 1] - t[i][j - 1]) / (x[i + j] - x[i])
    
    return t[0]

# Criação do polinômio interpolador
def Polinomio(x, c, horarios):
    
    n = len(horarios)
    polinomio = c[0]
    
    p = 1
    
    for i in range(1, n):
        p *= (x - horarios[i - 1])
        polinomio += c[i] * p
    
    return polinomio

# Cálculo dos coeficientes para tarde
coeficientesTarde = diferenca_dividida(horariosTarde, demandasTarde)

# Cálculo dos coeficientes para manhã
coeficientesManhã = diferenca_dividida(horariosManhã, demandasManhã)

horario_max_tarde = 13.74
demanda_max_tarde = Polinomio(horario_max_tarde, coeficientesTarde, horariosTarde)
horario_max_tarde1 = 13.75
demanda_max_tarde1 = Polinomio(horario_max_tarde1, coeficientesTarde, horariosTarde)
horario_max_tarde2 = 13.73
demanda_max_tarde2 = Polinomio(horario_max_tarde2, coeficientesTarde, horariosTarde)
print("Os 3 horários de demanda maxima pela tarde são:")
print(f"A demanda máxima de tarde às {horario_max_tarde}h é de aproximadamente {demanda_max_tarde} MW.")
print(f"A demanda máxima de tarde às {horario_max_tarde1}h é de aproximadamente {demanda_max_tarde1} MW.")
print(f"A demanda máxima de tarde às {horario_max_tarde2}h é de aproximadamente {demanda_max_tarde2} MW.")
print("\n")

horario_min_manhã = 6.76
demanda_min_manhã = Polinomio(horario_min_manhã, coeficientesManhã, horariosManhã)
horario_min_manhã1 = 6.77
demanda_min_manhã1 = Polinomio(horario_min_manhã1, coeficientesManhã, horariosManhã)
horario_min_manhã2 = 6.74
demanda_min_manhã2 = Polinomio(horario_min_manhã2, coeficientesManhã, horariosManhã)
print("Os 3 horários de demanda minima pela manhã são:")
print(f"A demanda minima de manhã às {horario_min_manhã}h é de aproximadamente {demanda_min_manhã} MW.")
print(f"A demanda minima de manhã às {horario_min_manhã1}h é de aproximadamente {demanda_min_manhã1} MW.")
print(f"A demanda minima de manhã às {horario_min_manhã2}h é de aproximadamente {demanda_min_manhã2} MW.")

