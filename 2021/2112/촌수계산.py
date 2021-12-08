import sys


def dfs(v):
    ans = [v]
    while 1:
        if v in pedigree:
            vp = pedigree[v]
            ans.append(vp)
            v = vp
        else:
            return ans


input = sys.stdin.readline
total = int(input())
a, b = map(int, input().split())
pedigree = {}
for n in range(int(input())):
    p, c = map(int, input().split())
    pedigree[c] = p
al = dfs(a)
bl = dfs(b)
flag=0
for i in range(len(bl)):
    if al[-1] == bl[i]:
        flag = 1
        bl = bl[:i + 1]
        c=len(set(al)&set(bl))
        print(len(set(al+bl))-c)
        break
if not flag:
    for j in range(len(al)):
        if bl[-1] == al[j]:
            flag = 1
            al = al[:j + 1]
            c = len(set(al) & set(bl))
            print(len(set(al + bl)) - c)
            break
if not flag:
    print(-1)