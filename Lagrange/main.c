#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double P=0, L=1, ponto, x[100], f[100];
    int i, j, n=4;

    printf("Digite o ponto a ser estimado:\n");
    scanf("%lf", &ponto);

    for(i=0; i<=n; i++)
    {
        printf("Insira o valor de x%d:\n", i);
        scanf("%lf",&x[i]);
        printf("Insira o valor de f(x%d):\n", i);
        scanf("%lf",&f[i]);
    }

    for(i=0; i<=n; i++)
    {
        for(j=0; j<=n; j++)
        {
            if(i!=j)
            {
                L *= ((ponto-x[j])/(x[i]-x[j]));
            }
        }
          P += (f[i]*L);
    }

    printf("%lf.", P);
    return 0;
}


