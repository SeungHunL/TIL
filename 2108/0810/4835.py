T = int(input().strip())
for num in range(T):
    N,M = map(int,input().split())
    Num_list = list(map(int, input().split()))
    real_h = low_s = 0
    for i in range(N-M+1):
        total = 0
        for j in range(i,i+M):
            total += Num_list[j]
        if real_h < total:
            real_h = total
        if low_s == 0:
            low_s = total
        elif low_s > total:
            low_s = total
    print(f'#{num+1} {real_h-low_s}')