#include <stdio.h>
int main()
{
 int i,start,end,k,g,arm;
 printf("enter the starting range :\n");
 scanf("%d",&start);
 printf("enter the end range:\n");
 scanf("%d",&end);
 for(i=start;i<=end;i++)
 {
     k=i;
     while(k>0)
     {
       g=k%10;
       arm=(g*g*g)+arm;
       k=k/10;
     }
     if(arm==i)
     {
         printf("%d,",arm);
     }
 }
 return 0;
}