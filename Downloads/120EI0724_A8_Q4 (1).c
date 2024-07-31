#include <stdio.h>
union unionJob
{
   char name[32];
   float salary;
   int workerNo;
} uJ;

struct structJob
{
   char name[32];
   float salary;
   int workerNo;
} sJ;

int main()
{
   printf("Size of union = %d bytes", sizeof(uJ));
   printf("\n Size of structure = %d bytes", sizeof(sJ));
   printf("\n");
   uJ.salary = 15.6;
   uJ.workerNo = 10;

   printf("Salary = %.1f\n", uJ.salary);
   printf("Number of workers = %d", uJ.workerNo);
   return 0;
}