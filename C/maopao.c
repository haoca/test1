#include <stdio.h>

//输入三个整数x,y,z，请把这三个数由小到大输出。
//利用冒泡排序

int main() {
    int number,n[100],t,i,j;
    printf("how many numbers do you have?\n");
    scanf("%d",&number);
    printf("you have %d numbers,please enter them.\n",number);
    for(i=0;i<number;i++){
        printf("[%d]:",i+1);
        scanf("%d",&n[i]);
        printf("\n");
    }
    for(i=0;i<number;i++){
        for(j=i+1;j<number;j++){
            if(n[i]>n[j]){
                t=n[i],n[i]=n[j],n[j]=t;
            }
        }
    }
    for(i=0;i<number;i++){
        printf("%d\n",n[i]);
    }
}