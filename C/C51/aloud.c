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
sbit beep = P3 ^ 7;
void main()
{
    int i = 1;
    while (i++ < 200)
    {

        beep = ~beep;
        delay(i);
    }
}