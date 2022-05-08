import sys

def permute(arr):
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            game(arr[:3]+[0]+arr[3:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

def game(arr):
    global max_score
    score=0
    now = -1
    for i in range(N):
        out = 0
        p = []
        this_inning = hit[i]
        while out<3:
            now += 1
            now %= 9
            n = this_inning[arr[now]]
            if n:
                p.append(n)
            else:
                out +=1
        if len(p)>3:
            score+=len(p)-3
            p=p[-3:]
        for i in range(len(p)):
            if sum(p[i:])>3:
                score+=1
            else:
                break
    max_score=max(max_score,score)

input = sys.stdin.readline

N = int(input())
hit=[]
max_score=0
for i in range(N):
    hit.append(list(map(int,input().split())))

permute([1,2,3,4,5,6,7,8])
print(max_score)