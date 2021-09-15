T = int(input())
A = B = C = 0
while T:
    if T >= 300:
        A = T // 300
        T %= 300
    elif T >= 60:
        B = T // 60
        T %= 60
    elif T >= 10:
        C = T // 10
        T %= 10
    else:
        print(-1)
        break
    if T == 0:
        print(f'{A} {B} {C}')
