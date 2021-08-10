T = int(input().strip())
for num in range(T):
    K,N,M = map(int,input().split())
    Charge = [0] * N
    Charge_list = list(map(int,input().split()))
    for i in Charge_list:
        Charge[i] +=1
    location = E = 0
    while location < N:
        if N-location <= K:
            break
        for g in range(K,0,-1):
            if Charge[location+g] == 1:
                E += 1
                location += g
                break
        else:
            E = 0
            break
    print(f'#{num+1} {E}')