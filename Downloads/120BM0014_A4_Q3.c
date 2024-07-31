#include <stdio.h>
int main()
{
   int k,sum=0,t,i;
   printf("enter any number to check perfect number-");
   scanf("%d",&k);
   for(i=1;i<=k;i++)
   {
       if(k%i==0)
       {
          t=k/i;
          printf("%d ",t);
          sum=sum+t;
       }
    }
    printf("the sum of the divisors are:%d\n",sum);
    if(k==(sum/2.0))
    {
        printf(" so this is a PERFECT! number");
    }
    else
    {
        printf("this is not a perfect number");
    }
    return 0;
}