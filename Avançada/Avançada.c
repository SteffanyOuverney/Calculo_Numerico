#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (log(x))//função
#define d2(x) (1/(pow(x,2)))//derivada segunda

int main()
{
    double x0, h, r, a, aprox=0, DA=0, DRP=0, errTrunc1=0, errTrunc2=0;

    printf("******** Formula da diferença avançada ********\n");
    printf("Digite os valores de x e h: ");
    scanf("%lf %lf", &x0, &h);
    printf("Digite o valor de referencia: ");
    scanf("%lf", &r);

    a = x0+h;

    aprox = (f(a)-f(x0))/h;

    printf("Aproximação f'(x): %lf\n", aprox);

    DA = fabs(r-aprox);
    DRP = fabs(((r-aprox)/r)*100);

    printf("Desvio absoluto: %e\n", DA);
    printf("Desvio relativo percentual: %lf %\n", DRP);

    errTrunc1 = fabs((h/2)*d2(x0));
    errTrunc2 = fabs((h/2)*d2(a));

    printf("%lf  %lf", errTrunc1, errTrunc2);
    if(errTrunc1 >= errTrunc2)
    {
        printf("Cota maxima de erro de truncamento: %e\n", errTrunc1);
    }
    else
    {
        printf("Cota maxima de erro de truncamento: %e\n", errTrunc2);
    }

    return 0;
}
