def s_cal(list1):
    a = 1
    for i in range(2):
        for j in range(i+1,3):
            a *= s_list[list1[i]][list1[j]]
    return round(a,2)

def casting(k,idx): # 조합으로 배우들 세트 생성
    if k == 3:
        synergy = s_cal(sel)
        b = 0
        for i in sel:
            b += mom_price[i]
        result.append([synergy] +[b]+sel) # 시너지값, 몸값합계, 0,1,2
        return
    for i in range(idx,n-3+k+1):
        sel[k] = i
        casting(k+1,i+1)

def last(k):
    global ans, flag
    if k == c:
        casting_cnt = [0] * n
        for i in range(c):
            if company_money[i] < last1[i][1]:
                return
            casting_cnt[last1[i][2]] += 1
            if casting_cnt[last1[i][2]] == 3:
                return
            casting_cnt[last1[i][3]] += 1
            if casting_cnt[last1[i][3]] == 3:
                return
            casting_cnt[last1[i][4]] += 1
            if casting_cnt[last1[i][4]] == 3:
                return

        ans = last1[0][1] + last1[1][1] + last1[2][1]
        flag = True
        return

    for i in range(z):
        last1[k] = result[i]
        if not flag:
            last(k+1)
        else:
            return


for tc in range(1,int(input())+1):
    n, s, c = map(int, input().split()) # n = 배우 수 , s = 시너지 상세 개수, c 회사개수
    s_list = [[1]*n for _ in range(n)] # 시너지표 빈 배열
    for _ in range(s): # 시너지 표 입력받아 채우기
        st , ed , st_s = map(float, input().split())
        st = int(st) -1
        ed = int(ed) -1
        s_list[st][ed] = st_s
        s_list[ed][st] = st_s
    mom_price = list(map(int,input().split())) # 배우별 몸값 리스트
    company_money = list(map(int, input().split())) # 회사별 예산 리스트
    sel = [0] * 3 # 배우 3명씩 뽑는 sel 리스트
    result = []
    casting(0,0)
    result.sort(key=lambda x: x[0], reverse=True)
    z = len(result)
    last1 = [0] * c # 빈리스트
    ans = 0
    flag = False
    last(0)

    print(f'#{tc} {ans}')