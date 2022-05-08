import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = []
for n in A:
    n -= B
    if n > 0:
        if n%C :
            p = n//C + 2
        else:
            p = n//C + 1
    else:
        p = 1
    ans.append(p)
print(sum(ans))

