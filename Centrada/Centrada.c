#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (exp(-2*x)+cos(2*x))//função
#define d3(x)(-8*exp(-2*x)+8*sin(2*x))//derivada terceira

int main()
{
    double x0, h, r, a, b, aprox=0, DA=0, DRP=0, errTrunc1=0, errTrunc2=0;

    printf("******** Formula de tres pontos centrada ********\n");
    printf("Digite os valores de x e h: ");
    scanf("%lf %lf", &x0, &h);
    printf("Digite o valor de referencia: ");
    scanf("%lf", &r);

    a = x0+h;
    b = x0-h;

    aprox = ((f(a))-(f(b)))/(2*h);

    printf("Aproximação f'(x): %lf\n", aprox);

    DA = fabs(r-aprox);
    DRP = fabs(((r-aprox)/r)*100);

    printf("Desvio absoluto: %e\n", DA);
    printf("Desvio relativo percentual: %lf\n", DRP);

    errTrunc1 = fabs((pow(h,2)/6)*d3(b));
    errTrunc2 = fabs((pow(h,2)/6)*d3(a));

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
