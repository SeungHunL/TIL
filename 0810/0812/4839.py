def mis(F, D):
    cnt = 0
    l = 1
    while l <= F:
        c = int((l + F) / 2)
        cnt += 1
        if c == D:
            return cnt
        elif c > D:
            F = c
        else:
            l = c

T = int(input())
for num in range(T):
    P, A, B = map(int, input().split())
    l = 1
    r = B
    print(mis(P,A),mis(P,B))
    if mis(P, A) < mis(P, B):
        print(f'#{num + 1} A')
    elif mis(P, A) == mis(P, B):
        print(f'#{num + 1} 0')
    else:
        print(f'#{num + 1} B')
