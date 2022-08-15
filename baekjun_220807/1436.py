import sys

input = sys.stdin.readline

N = int(input())
num=665
while N:
    num+=1
    if "666" in str(num):
        N-=1
    if N==0:
        print(str(num))