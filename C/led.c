#include <reg52.h>
#include <intrins.h>
//sbit LED = P0^1;
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
    // int beep = 0;
    int temp = 0x7F;
    // while (1)
    // {
    //     beep = 0; //将电平取反：P15端口具有上拉，上拉电阻默认为高电平，输入到IN5，则输出为低电平；在while循环中不断有高低电平的变换，则产生脉冲
    //     // delay(115);   //改变周期-->音色
    // }
    while (1)
    {
        P0 = temp;
        beep = ~beep;
        delay(500);
        P0 = _crol_(P0, 1);
        temp = P0;
        delay(500);
        //LED = 0;
    }
}