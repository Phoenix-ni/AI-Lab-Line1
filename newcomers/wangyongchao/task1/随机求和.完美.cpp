#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int contains(int arr[],int len,int num);
int main()
{
	srand(time(NULL));
	int arr[10]={0};
	int len=sizeof(arr)/sizeof(int);
	int sum=0;
	for(int i=0;i<len;)
	{
		int num=rand()%100+1;
		int flag=contains(arr,len,num);
	if(!flag)	
	{
		arr[i]=num;
		i++;
	}
	}
	for(int i=0;i<len;i++)
	{
		sum+=arr[i];
	}
	printf("%d\n",sum);
	int count=0;
	int avg=sum/len;
	for(int i=0;i<len;i++)
{
	if(arr[i]<avg)
	{
		count++;
	}
	
	
}
printf("平均数为%d\n",avg);
printf("%d\n",count);
	return 0;
}

int contains(int arr[],int len,int num)
{
	for(int i=0;i<len;i++)
	{
	
	if(num==arr[i])
	{
		return 1;
		
	}
}
	return 0;
 } 
