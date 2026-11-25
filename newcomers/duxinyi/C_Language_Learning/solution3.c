#include<stdio.h>
// 有n个整数，编写一个函数使其向右循环移动m个位置
int *solve(int *s,int n,int m){
    int temp[n];
    for (int i=0; i<n; i++){
        temp[i]=s[i];
    }//将原数组复制到临时数组中
    for (int i=0; i<n; i++){
        if (i<m){
            s[i] = temp[n-m+i];
            //将原本最后m个数放到最前面
        }
        else s[i] = temp[i-m];
        //将原本的前n-m个数放到后面
    }
    return s;
}


int main(void)
{
    int n,m,s[110];
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;i++)
        scanf("%d",&s[i]);

    int *ans;
    ans = solve(s, n, m);

    for(int i=0;i<n;i++){
        if(i==0)    printf("%d",*ans++ );
        else    printf(" %d",*ans++ );
    }
    return 0;
}