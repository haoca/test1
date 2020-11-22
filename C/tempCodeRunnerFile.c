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
    int i, ledtab[] = {0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0xff};
    while (1)
    {
        P1 = 0xEE;
        P0 = ledtab[i++];
        if (i == 9)
        {
            i = 0;
        }
        delay(1000);

        /* code */
    }
}