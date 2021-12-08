T = int(input().strip())
for num in range(T):
    N = int,input()
    card = list(map(int,list(input())))
    cardnum=[0]*10
    for i in card:
        cardnum[i]+=1
    Mx = cNum = 0
    for i in range(0,len(cardnum)):
        if Mx <= cardnum[i]:
            if cNum> i:
                cNum = i
            Mx = cardnum[i]
            cNum = i
    print(f'#{num+1} {cNum} {Mx}')