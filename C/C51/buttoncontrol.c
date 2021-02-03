#include <reg52.h>
#include <intrins.h>
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
int touch1(key) //判断按下
{
    if (key == 0)
    {
        delay(10);
        if (key == 0)
        {

            while (!key4)
                ;
            delay(10);
            while (!key4)
                ;
            return 1;
        }
    }
    else
        return 0;
}

void main()
{
    int temp, i = 1;
    temp = 0xFE;
    P0 = temp;
    key4 = 1;
    while (1)
    {
        if (touch1(key4))
        {
            temp = _crol_(temp, 1);
            P0 = temp;
        }
    }
}