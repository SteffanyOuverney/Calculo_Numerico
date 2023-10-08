# Mostre que dado a fun¸c˜ao abaixo existe valores para os coeficientes a, b, c, e d que torne f(x) uma interpolação com o metodo de spline cubica.

#(a) Mostre quais s˜ao estes valores para a, b, c, e d.
#(b) Mostre o polinˆomio interpolador.

import sympy as sp

x0 = -2
x1 = -1
x2 = 1
x3 = 2


a, b, c, d = sp.symbols('a b c d')

# Definindo as funções da spline S(x) 
S0 = (x + 1)**3
S1 = a*(x**3) + b*(x**2) + c*x + d
S2 = (x - 1)**2

# Calculando a primeira derivada
df1_s0 = sp.diff(S0, x)
df1_s1 = sp.diff(S1, x)
df1_s2 = sp.diff(S2, x)

# Calculando a segunda derivada
df2_s0 = sp.diff(df1_s0, x)
df2_s1 = sp.diff(df1_s1, x)
df2_s2 =sp.diff(df1_s2, x)

# S0(x0) = f(x0) e S1(x1) = f(x1) ou S0(x1) = S1(x1)
Passo1_S0_x0 = S0.subs(x, x0)
Passo1_S1_x1 = S1.subs(x, x1)
#print(Passo1_S0_x0)
#print(Passo1_S1_x1)

# S0(x1) = S1(x1) e S1(x2) = S2(x2)
Passo1_S1_x2 = S1.subs(x, x2)
#print(Passo1_S1_x2)

# S0'(x1) = S1'(x1)
Passo2_S1_x1 = df1_s1.subs(x, x1)
#print(Passo2_S1_x1)

# S1'(x2) = S2'(x2)
Passo3_S1_x2 = df1_s1.subs(x, x2)
#print(Passo3_S1_x2)

# S0''(x1) = S1''(x1)
Passo4_S0_x1 = df2_s1.subs(x, x1)
#print(Passo4_S0_x1)

# S1''(x2) = S2''(x2)
Passo5_S1_x2 = df2_s1.subs(x, x2)
print(Passo5_S1_x2)
