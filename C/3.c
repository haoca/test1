#include <stdio.h>
#include <math.h>
#include <time.h>
int main()
{
    int a = 1111, b = 2222;
    int sum = a + b * 6;
    printf("%d\n", sum);
    printf("Time used=%.5f\n", (double)clock() / CLOCKS_PER_SEC);
    return 0;
}
