import sys
def square(n):
    global maps
    l = 2**n
    nmap=[[0]*2**N for _ in range(2**N)]
    melted=[] # 이미 녹은 좌표
    for i in range(N//n+1): #작은 네모 설정
        for j in range(N // n+1):
            for k in range(l):
                for m in range(l):
                    ice = maps[l*i+k][l*j+m]
                    if ice==0:
                        melted.append([l*i+m,l*j+l-1-k])
                    nmap[m][l-1-k]=maps[k][m]

    edges=([0,0],[2**N-1,0],[0,2**N-1],[2**N-1,2**N-1])
    for i in range()

    d = [(-1,0),(1,0),(0,1),(0,-1)]
    for i, j in melted:
        for dy, dx in d:
            my = i + dy
            mx = j + dx
            if 0 <= my < 2 ** N and 0 <= mx < 2 ** N and nmap[my][mx]:
                nmap[my][mx]-=1


                c = 0
                for ty, tx in d:
                    if 0 <= my + ty < 2 ** N and 0 <= mx + tx < 2 ** N:
                        if nmap[my + ty][mx + tx] == 0:
                            c += 1
                    else:
                        c += 1
                if c >= 2:
                    nmap[my][mx] -= 1

    maps=nmap

input = sys.stdin.readline
N,Q = map(int,input().split())
maps=[]
for i in range(2**N):
    maps.append(list(map(int,input().split())))
level = list(map(int,input().split()))

for l in level:
    square(l)

ans1=0
ans2 = 0
for i in maps:
    ans1+=sum(i)
    if ans2 < max(i):
        ans2=max(i)

print(ans1)
print(ans2)