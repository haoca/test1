#include <stdio.h>

void pyramid( int n );

int main()
{    
    int n;

    scanf("%d", &n);
    pyramid(n);

    return 0;
}
void pyramid( int n ){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<(n-i-1);j++){
            printf(" ");
        }
        for(j=0;j<i+1;j++){
            printf("%d ",i+1);
        }
        printf("\n");
    }
}
/* 你的代码将被嵌在这里 */