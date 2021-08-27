import sys
bulb_n = int(sys.stdin.readline())
bulb = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
for _ in range(N):
    S, a = map(int, sys.stdin.readline().split())
    if S == 1:
        for i in range(1, 1 + bulb_n // a):
            bulb[a * i - 1] = 1 - bulb[a * i - 1]
    else:
        j = 1
        bulb[a - 1] = 1 - bulb[a - 1]
        while a - j - 1 >= 0 and a + j - 1 <= bulb_n - 1 and bulb[a - j - 1] == bulb[a + j - 1]:
            bulb[a - j - 1] = 1 - bulb[a - j - 1]
            bulb[a + j - 1] = bulb[a - j - 1]
            j += 1
for E in range(bulb_n):
    if not (E+1)%20:
        print(bulb[E])
    else:
        print(bulb[E],end=' ')

