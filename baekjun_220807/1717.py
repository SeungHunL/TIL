import sys


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for i in range(m):
    s, a, b = map(int, input().split())
    if a==b:
        if s:
            print("YES")
        continue
    if s:
        print("YES") if find(a) == find(b) else print("NO")
    else:
        union(a, b)
