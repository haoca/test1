#include <reg52.h>

#include <intrins.h>
void delay(unsigned int t)
{
    unsigned int i, j;
    for (i = t; i > 0; i--)
    {
        for (j = 120; j > 0; j--)
        {
        }
    }
}
void main()
{
    int temp, i;
    temp = 0xFE;
    P0 = temp;
    while (1)
    {

        temp = _crol_(temp, 1);
        delay(1000);
        P0 = temp;
        /* code */
    }
}