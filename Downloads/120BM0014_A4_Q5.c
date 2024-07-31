#include <stdio.h>
int main()
{
  int m,f=0,i,s=1,k=0;
  printf("enter the no of terms to be displayed-");
  scanf("%d",&m);
  printf("so the fibonacee series is: 0 1 ");
  for(i=1;i<=m;i++)
  {
    k=f+s;
    printf("%d ",k);
    f=s;
    s=k;
  }
  return 0;
}