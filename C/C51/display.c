#include <reg52.h>
sbit key4 = P2 ^ 0;
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
int touch(key) //判断按下
{
    if (key == 0)
    {
        delay(10);

        while (!key4)
            ;
        delay(10);
        while (!key4)
            ;

        return 1;
    }
    else
        return 0;
}
void main()
{
    int i, ledtab[] = {0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0xff};
    while (1)
    {
        P1 = 0xFE;
        if (touch(key4))
            P0 = ledtab[i++];
        if (i == 10)
        {
            i = 0;
        }
        // delay(1000);

        /* code */
    }
}