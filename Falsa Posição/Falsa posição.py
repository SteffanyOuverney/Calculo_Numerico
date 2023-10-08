import math
import matplotlib.pyplot as plt

#calcula o valor na função
def f(x):

    f = (x**3)-9*x+5; #Insira a função

    return f;

print("******** Metodo da Falsa posição ********\n");
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

if(f(x0)*f(x1)<0):

    x = ((x0*f(x1))-(x1*f(x0)))/(f(x1)-f(x0));

    while((x1-x0) or (abs(f(x)))>tol):

        if(f(x0)*f(x)<0):
            x1 = x;
        if(f(x0)*f(x)>0):
            x0 = x;
        
        x = ((x0*f(x1))-(x1*f(x0)))/(f(x1)-f(x0));
        
        if(f(x)<tol):
            break;

    print("A raiz é %lf.\n" %x);
else:
    print("Não há raizes no intervalo.")

plt.show();



