import sys

input = sys.stdin.readline

N = int(input())
ss = []
for i in range(N):
    ss.append(int(input()))
score = [0] * N
if N==1:
    print(ss[0])
elif N==2:
    print(ss[0]+ss[1])
elif N==3:
    print(max(ss[0] + ss[2], ss[1] + ss[2]))
else:
    score[0] = ss[0]
    score[1] = ss[0] + ss[1]
    score[2] = max(ss[0] + ss[2], ss[1] + ss[2])
    for i in range(3, N):
        score[i] = max(score[i - 3] + ss[i - 1] + ss[i], score[i-2] + ss[i])
    print(score[-1])
