import math
import matplotlib.pyplot as plt

#calcula o valor na função
def f(x):

    f = (x**3)-9*x+5; #Insira a função

    return f;

print("******** Metodo da Secante ********\n");
print("Digite o valor inicial x0, x1 e a tolerancia: ");
x0 = float(input());
x1 = float(input());
tol = float(input());

#pontos a serem plotados
x = [1, 3, 8];
y = [f(1), f(3), f(8)];

plt.plot(x, y);
plt.xlabel('x');
plt.ylabel('f(x)');
plt.title('Gráfico f(x) vs. x');

i=2;
max_iter = 100;

if(f(x0)*f(x1)<0):

    while(i<=max_iter):

        x = x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)));

        if(abs(x-x1)<tol):
            print("A raiz é %lf.\n" %x);
            break;

        i+=1;

        x0 = x1;
        x1 = x;
else:
    print("Não há raizes no intervalo.")

plt.show();
