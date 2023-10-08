import math
import matplotlib.pyplot as plt

def f(x):

    f = (x**3)-9*x+5; #Insira a função

    return f;

itera=100;
i=1;

print("******** Metodo da Bisseccao ********\n\n");
print("Digite o valor do intervalo [a,b] e a tolerancia: ");
a = float(input());
b = float(input());
tol = float(input());

if(f(a)*f(b) > 0):

    print("O intervalo [a,b] é inválido.\n");
    print("Por favor, digite o valor do intervalo [a,b]:\n");
    a = float(input());
    b = float(input());
    tol = float(input());  

#pontos a serem plotados
x = [1, 3, 8];
y = [f(1), f(3), f(8)];

plt.plot(x, y);
plt.xlabel('X');
plt.ylabel('f(x)');
plt.title('Gráfico f(x) vs. x');

while((i<=itera)):

    raiz = a+((b-a)/2);

    if((f(a))*(f(raiz)) > 0):
    
        a = raiz;
    
    else:
    
        b = raiz;
    
    if((f(raiz) == 0) or (((b-a)/2) < tol)):
    
        print("A raiz da função é: %.9f." %raiz);
        break;
    
    i+=1;

plt.show();