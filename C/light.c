#include <reg52.h>
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
    int temp, i, ledtab[] = {0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0xff};
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