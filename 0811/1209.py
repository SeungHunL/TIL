for num in range(10):
    T = int(input())
    bingo = []
    for u in range(100):
        sbing = list(map(int,input().split()))
        bingo.extend(sbing)
        sbing = []
    mx = 0
    for i in range(100):
        galo = 0
        selo = 0
        for j in range(100):
            galo += bingo[100*i+j]
            selo += bingo[i+j*100]
        if mx <= galo and galo >= selo:
            mx = galo
        elif mx < selo and selo > galo:
            mx = selo
    daegag = 0
    daegag2 = 0
    for k in range(100):
        daegag += bingo[101*k]
        daegag2 += bingo[99*(k+1)]
    if mx <= daegag and daegag >= daegag2:
        mx = daegag
    elif mx < daegag2 and daegag2 > daegag:
        mx = daegag2
    print(f'#{T} {mx}')