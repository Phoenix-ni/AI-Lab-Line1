#include<stdio.h>
// 用一个函数实现两个字符串的比较，即自己写一个strcmp函数
int strcmp(char *p1,char *p2){
    int result = 0;

    while(*p1 !='\0' || *p2 !='\0'){
        //p1结束了，p2还没结束
        if (*p1 =='\0' && *p2 != '\0'){
            result -= *p2;
            p2 ++;//p2继续读取
        }
        //p2结束了，p1还没结束
        else if(*p1 !='\0' && *p2 == '\0'){
            result += *p1;
            p1 ++;//p1继续读取
        }
        //都没结束
        else{
            result += *p1 -*p2;
            p1 ++; p2 ++;
        }  
    }
    return result;//返回字符串大小差值
}


int main(void)
{
	char a[110],b[110];
	scanf("%s%s",a,b);
	if(strcmp(a,b)>0)
		printf("%s", a);
	else
		printf("%s", b);
    return 0;
}