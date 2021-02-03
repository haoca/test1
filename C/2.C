#include <stdio.h>
union abc
{
    short a;
    char b[2];
};
int main()
{
    union abc abc1;
    printf("")
        /* data */
        abc1.a = 3;
    printf("%d and %d ", abc1.b[0], abc1.b[1]);
    int nums = 1, target = 9;
    //int a, count = 0;
    int num[5] = {0};
    //a = sizeof(num) / 4;
    //printf("%d and %d", sizeof(num), a);
}