#include <stdio.h>
int main()
{
  int i,j,k;
  printf("enter the number till which the table has to be shown-\n");
  scanf("%d",&k);
  for(i=1;i<=10;i++)
  {
    for(j=1;j<=k;j++)
	{
	  printf("%d x %d= %d  ",j,i,j*i);
	}
	printf("\n");
  }
  return 0;
}