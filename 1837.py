"""
#include <stdio.h>
int main()
{
  int a,b,c,gcd;
  scanf("%d %d",&a, &b);
  if(a==0)gcd=a;
  else if(b==0) gcd=b;
  else{
     while(b!=0){
         c=b;
         b=a%b;
         a=c;
     }
     gcd=a;
  }
  printf("GCD : %d\n",gcd);
  return 0;

  M = a
if a == 0:
    gcd = a
elif b == 0:
    gcd = b
else:
    while b != 0:
        c = b
        b = a % b
        a = c
    gcd = a
    print(gcd, (M % gcd))

}
a = b × q + r
0 ≤ r < |b|
"""
global r, q, f
X = input().split(" ")
a = int(X[0])
b = int(X[1])
if a < 0:
    print("if")
    e = b
    if b < 0:
        e = b * -1
    for r in range(e):
        f = a - r
        if f % b == 0:
            break
    q = f // b
else:
    print("else")
    print(a, b)
    q = a // b  # quotient
    r = a % b  # remainder

print(q, r)
