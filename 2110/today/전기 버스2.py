def go(location):
    c = 0
    location = 0
    e = charge[location]
    while location < N-1:

        maxd = 0
        flag=0

        for i in range(1,e+1):
            if location+i>=N-1:
                flag=1
                break
            d = location + charge[location + i]
            if d > maxd:
                maxi = i
                maxd = d
        if flag:
            break

        c += 1
        location += maxi  # 선택지 중 최대 거리를 가게 하는 충전소
        e = charge[location]
    return c


for q in range(int(input())):
    com = list(map(int, input().split()))
    N=com[0]
    charge=com[1:]
    print(f'#{q + 1} {go(N)}')
