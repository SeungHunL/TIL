import sys

N = int(sys.stdin.readline())
W = H = 0
D_stack = []
L_stack = []
for _ in range(6):
    D, L = map(int, sys.stdin.readline().split())
    if D == 4:
        H += L
    elif D == 1:
        W += L
    D_stack.append(D)
    L_stack.append(L)
    S = H * W

for i in range(6):
    if D_stack[i] == D_stack[(i + 2) % 6] and D_stack[(i + 1) % 6] == D_stack[(i + 3) % 6]:
        S -= L_stack[(i + 2) % 6] * L_stack[(i + 1) % 6]
print(S*N)
