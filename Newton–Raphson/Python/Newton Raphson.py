import math
import matplotlib.pyplot as plt

#calcula o valor na função
def f(x):

    f = 4*math.cos(x)-math.exp(x); #Insira a função

    return f;
#calcula o valor na derivada
def d(x):

    f = -4*math.sin(x)-math.exp(x); #Insira a derivada

    return f;

itera=100;
i=1;

print("******** Metodo de Newton Raphson********\n\n");
print("Digite o valor inicial x0 e a tolerancia: ");
x0 = float(input());
tol = float(input());

x = [1, 3, 8];
y = [f(1), f(3), f(8)];

plt.plot(x, y);
plt.xlabel('x');
plt.ylabel('f(x)');
plt.title('Gráfico f(x) vs. x');

for i in range(itera):

    x = x0-((f(x0))/(d(x0)));

    x0 = x;

print("O valor da aproximação é %.4lf." %x);

plt.show();