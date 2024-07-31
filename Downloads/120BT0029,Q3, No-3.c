#include<stdio.h>
int main() 
{
 int arr[50][50];
 int n;
 scanf("%d", &n);
 for(int i=0; i<n; ++i) {
 for(int j=0; j<n; ++j) {
 scanf("%d", &arr[i][j]);
 }
 }
 int x=-1, y=-1;
 int l=0;
 for(int i=0; i<n-1; ++i) {
 for(int j=0; j<n-1; ++j) {
 if(arr[i][j]==1) {
 for(int p=i+1; p<n; ++p) {
 for(int q=j+1; q<n; ++q) {
 if(arr[p][q] == 1 && p-i + q-j > l) {
 x=i;
y=j;
l=p-i+q-j;
 }
 }
 }
 }
 }
 }
 printf("%d %d %d\n", x, y, l);
}
//120BT0029_Q3_3

