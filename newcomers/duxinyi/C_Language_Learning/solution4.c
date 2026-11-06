#include<stdio.h>
//读入n(1 <= n <= 1000)个学生的成绩，成绩都为整数
//用指针函数求出若干个学生成绩的最高分，并输出最高分
int* sort_scores(int* s,int n){
    for (int i=0; i<n-1; i++){
        int temp;
        for (int j=0; j<n-i-1; j++){
            if (s[j] < s[j+1]){
                temp = s[j];
                s[j] = s[j+1];
                s[j+1] = temp;
            }
        }
    }
    return s;
}
int main(void)
{
    int n,s[110];
    scanf("%d",&n);
    for (int i=0;i<n;i++){ 
        scanf("%d",&s[i]);
    }
	int* p = sort_scores(s,n);
    printf("%d",*p);
    return 0;
}