#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (x*exp(-2*x))//função
#define d3(x) (exp(-2*x)*(12-8*x))//derivada terceira

int main()
{
    double x0, h, r, a, b, aprox=0, DA=0, DRP=0, errTrunc1=0, errTrunc2=0;

    printf("******** Formula de tres pontos nao centrada ********\n");
    printf("Digite os valores de x e h: ");
    scanf("%lf %lf", &x0, &h);
    printf("Digite o valor de referencia: ");
    scanf("%lf", &r);

    a = x0+h;
    b = x0 +(2*h);

    aprox =(-3*f(x0)-f(b))/(2*h)+(2*f(a))/h;

    printf("Aproximação f'(x): %lf\n", aprox);

    DA = fabs(r-aprox);
    DRP = fabs(((r-aprox)/r)*100);

    printf("Desvio absoluto: %e\n", DA);
    printf("Desvio relativo percentual: %lf\n", DRP);

    errTrunc1 = fabs((pow(h,2)/3)*d3(x0));
    errTrunc2 = fabs((pow(h,2)/3)*d3(x0+2*h));

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
