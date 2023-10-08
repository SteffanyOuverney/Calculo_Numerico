#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (pow(x,3)-9*x-3) //fun��o
#define d(x) (3*pow(x,2)-9) //derivada da fun��o

int main()
{
    //declara��o de vari�veis
    double x0=0, x=0, tolerancia=0;
    int i, itera=100;

    printf("******** Metodo Newton-Raphson ********\n\n");
    printf("Digite o valor de x e a tolerancia:\n");
    scanf("%lf %lf", &x0, &tolerancia);

    for(i=1; i<=itera; i++)
    {
        x = x0-((f(x0))/(d(x0)));

        x0 = x;
    }

    printf("\nA solucao para a funcao e %lf.\n", x);

    return 0;
}


