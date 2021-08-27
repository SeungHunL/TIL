for _ in range(int(input())):
    N = int(input())
    s = 0
    v = 0
    for __ in range(N):
        command= list(map(int, input().split()))
        if command[0] == 1:
            v += command[1]
            s += v
        elif command[0] == 2:
            v -= command[1]
            if v<0:v=0
            s += v
        else:
            s += v
    print(f'#{_+1} {s}')