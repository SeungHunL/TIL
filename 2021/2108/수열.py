import sys

N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
total = 0
for i in range(K):
    total += S[i]
mx = total
for j in range(0, N - K):
    total = total + S[j + K] - S[j]
    if mx < total:
        mx = total
print(mx)
