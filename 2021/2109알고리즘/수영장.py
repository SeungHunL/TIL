T = int(input())
for _ in range(T):
    oned, onem, threem, oney = map(int, input().split())
    cal = list(map(int, input().split()))
    mn = 100000

    # 1일 1달 비교
    for i in range(12):
        if cal[i]:
            if onem < oned * cal[i]:
                cal[i] = onem
            else:
                cal[i] = oned * cal[i]

    # 1달 3달 비교
    calp = [0] * 12
    calp[0] = cal[0]
    calp[1] = cal[0] + cal[1]
    if cal[2] + cal[1] + cal[0] > threem:
        calp[2] = threem
    else:
        calp[2] = cal[2] + cal[1] + cal[0]

    for j in range(3, 12):
        thd = cal[j] + cal[j - 1] + cal[j - 2] + calp[j - 3]
        ond = cal[j] + calp[j - 1]
        thm = threem + calp[j - 3]
        if thd > ond and thm > ond:
            calp[j] = ond
        elif thd > thm:
            calp[j] = thm
        else:
            calp[j] = thd

    # 1년 비교
    if calp[11] > oney:
        ans = oney
    else:
        ans = calp[11]

    print(f'#{_ + 1} {ans}')
