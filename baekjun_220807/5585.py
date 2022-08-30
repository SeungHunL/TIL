import sys

input = sys.stdin.readline

N = int(input())
c=0
n=1000-N
cs=[500,100,50,10,5,1]
for coin in cs:
    r=n//coin
    c+=r
    n-=coin*r
print(c)