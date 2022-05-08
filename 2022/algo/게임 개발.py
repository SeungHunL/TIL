import sys
def square(n):
    return

input = sys.stdin.readline
N = int(input())
bs=[]
ans = [0]*N
days = 0
for i in range(N):
    bs.append(list(map(int,input().split()))[:-1])

while N:
    for i in range(len(bs)):
        if not ans[i]:
            for j in bs[i][1:]:
                if not ans[j]:
                    break
            else:
                ans[i] = days +bs[i][0]
                N-=1

for i in ans:
    print(i)
print(bs)

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 10
# 20
# 14
# 18
# 17