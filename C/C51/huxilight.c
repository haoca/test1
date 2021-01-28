#include <reg52.h>
#include <intrins.h>
#define uchar unsigned char
#define uint unsigned int
uint n = 0;
// sbit LED = P0 ^ 0;
uint i, pwm, y = 500, temp;

void delay(uint i) //延时函数
{
    int x;
    for (x = i; x > 0; x--)
        ;
}
void main()
{
    temp = 0xFE;
    P0 = temp;
    while (1)
    {

        for (pwm = 0; pwm < y; pwm++)
        {
            P0 = temp;
            delay(pwm);

            P0 = 0xFF;
            delay(y - pwm);
        }
        for (pwm = y; pwm > 0; pwm--) //逐渐变暗
        {
            //LED = 0; //灯亮
            // temp = _crol_(temp, 1);

            P0 = temp;
            delay(pwm);
            // LED = 1; //灯灭
            P0 = 0xFF;
            delay(y - pwm);
        }

        temp = _crol_(temp, 1);
        delay(150);
    }
}