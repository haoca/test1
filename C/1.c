#include <stdio.h>
#include <stdlib.h>
// qrecall(6)
// {
//     int b;
//     b = a + 3;
//     return b;
// }
int main()
{
    // b = 5;
    // int dd = 3, 5, 6;
    // printf("%d", dd);
    int a = 0, j, i, (*p)[3];

    int c[4][3] = {0};
    p = c;
    for (j = 0; j < 4; j++)
    {
        for (i = 0; i < 3; i++)
        {
            printf("%d\n", p[0][3 * i + j]);
        }
    }
    printf("%d\n%d\n", c + 1, *(c + 1));

    int cc[] = {5, 4, 7, 8};
    a = sizeof(cc) / sizeof(cc[0]);
    printf("%d", a);

    // scanf("%d", &a);
    // // printf("nihao\n%d\n%o\n%x\n", a, a, a);
    // printf("%d", recall(a));
    //scanf("%d",&b);
}