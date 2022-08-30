import sys

input = sys.stdin.readline
N,K=map(int,input().split())
coins=[]
for _ in range(N):
    coin=int(input())
    if coin<=K:
        coins.append(coin)
coins=coins[::-1]
dp=[0]*len(coins)
tmp=0
for coin in coins:
    n= K//coin
    tmp+=n
    K-=n*coin
print(tmp)

