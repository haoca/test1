#include <stdio.h>

int sushu(int a)
{
    int i = 0;
    int k = 1;
    for (i = 2; i < a; i++)
    {
        if (a % i == 0)
            k = 0;
        //printf("%d\n",k);
    }
    return k;
}
int main()
{
    int a, i;
    scanf("%d", &a);
    if (a > 1)
    {
        for (i = 2; i <= a; i++)
        {
            if (sushu(i))
                printf("{%d} is sushu\n", i);
        }
    }
    else
        printf("no sushu");
    return 0;
}
