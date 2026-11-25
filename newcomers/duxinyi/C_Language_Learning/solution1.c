#include<stdio.h>
// 有n人围成一圈，从1开始顺序编号
// 从第1个人开始报数（从1到3报数），凡报到3的人退出圈子
// 问最后留下的是原来的第几号的那位
int main(void)
{
    //定义与初始化
    int n;
    scanf("%d",&n);
    int arr[n];
    int total = n;
    for(int i =0; i<n; i++){
        arr[i]=0;
    }

    int *p = arr;
    int count = 0;
    while (total>1){
        for(int i=0; i<n; i++){
            if (*(p+i) == -1) continue;//跳过已经退出圈子的
            count ++;//1-3报数
            if (count == 3){
                *(p+i) = -1;
                count = 0;
                total --;
            }//报到3的标记，开始下一轮计数
        }
    }
    
    for(int i=0; i<n; i++){
        if(*(p+i)!=-1){
            printf("%d",i+1);
        }//打印最后留下来人原来的编号
    }
    return 0;
}