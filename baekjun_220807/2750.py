import sys

input=sys.stdin.readline

N=int(input())
nums=[]
for i in range(N):
   nums.append(int(input()))
nums.sort()
for i in nums:
    print(i)