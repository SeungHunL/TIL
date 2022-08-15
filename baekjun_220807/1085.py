import sys

input = sys.stdin.readline

x,y,w,h = map(int, input().split())
ans = min(x,w-x,y,h-y)
print(ans)
