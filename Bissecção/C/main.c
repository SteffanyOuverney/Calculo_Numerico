#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (pow(x,3)-7*pow(x,2)+(14*x)-6)

int main()
{
    //declara��o de vari�veis
    double a=0, b=0, tol, raiz;
    int itera =100, i=1;

    printf("******** Metodo da Bisseccao ********\n\n");
    printf("Digite o valor do intervalo [a,b] e a tolerancia:\n");
    scanf("%lf %lf %lf", &a, &b, &tol);

    if(f(a)*f(b) > 0)
    {
        printf("O intervalo [a,b] e invalido.\n");
        printf("Por favor, digite o valor do intervalo [a,b]:\n");
        scanf("%f %f %f", &a, &b, &tol);
    }

    while((i<=itera))
    {
        raiz = a+((b-a)/2);

        if((f(a))*(f(raiz)) > 0)
        {
            a = raiz;
        }
        else
        {
            b = raiz;
        }
         if((f(raiz) == 0) || (((b-a)/2) < tol))
        {
            printf("A raiz da fun��o �: %.9f.", raiz);
            break;
        }
        i++;
    }
    return 0;
}
