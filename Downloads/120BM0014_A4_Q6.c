#include <stdio.h>
int main()
{
  int m,rm=0,s,d;
  printf("enter a numbe:");
  scanf("%d",&m);
  s=m;
  while(m>0)
  {
    d=m%10;
    rm=(rm*10)+d;
    m=m/10;
  }
  if(rm==s)
  {
      printf("this is a palindrome");
  }
  else
  {
      printf("this is not palindrome");
  }
  return 0;
}
