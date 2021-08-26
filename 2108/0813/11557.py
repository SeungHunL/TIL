T = int(input())
for _ in range(T):
    N = int(input())
    Mx = 0
    drunk = ''
    for i in range(N):
        C, S = input().split()
        if Mx < int(S):
            Mx = int(S)
            drunk = C
    print(drunk)
