import sys

input = sys.stdin.readline

N = int(input())
k = int(input())
s = 1
e = k

while s<=e:
    m = (s + e) // 2
    tmp = 0
    for i in range(1, N + 1):
        tmp += min(m // i, N)

    if tmp >= k:
        ans=m
        e = m-1
    else:
        s = m+1
print(ans)
