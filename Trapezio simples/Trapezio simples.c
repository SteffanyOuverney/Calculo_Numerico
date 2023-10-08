#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (exp(x)) //função a ser integrada
#define d2(x) (exp(x)) //derivada de segunda

int main()
{
    double x0, x1, h=0, aprox=0, r, DA=0, DRP=0, errTrunc1=0, errTrunc2=0;

    printf("******** Metodo do Trapezio simples ********\n\n");
    printf("Digite o valor de a e b: ");
    scanf("%lf %lf", &x0, &x1);
    printf("Digite o valor de referencia: ");
    scanf("%lf", &r);

    h = x1-x0;

    aprox = (h/2)*((f(x0))+(f(x1)));

    printf("O valor da aproximacao da integral: %lf\n", aprox);

    DA = fabs(r-aprox);
    DRP = fabs(((r-aprox)/r)*100);

    printf("Desvio absoluto: %e\n", DA);
    printf("Desvio relativo percentual: %lf\n", DRP);

    //erro de truncamento
    errTrunc1 = fabs(((pow(h,3))/12)*(d2(x0)));
    errTrunc2 = fabs(((pow(h,3))/12)*(d2(x1)));

    if(errTrunc1 >= errTrunc2)
    {
        printf("Cota maxima de erro de truncamento: %e\n", errTrunc1);
    }
    else
    {
        printf("Cota maxima de erro de truncamento: %e\n ", errTrunc2);
    }

    return 0;
}
