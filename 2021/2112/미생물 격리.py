for tc in range(int(input())):
    N, M, K = map(int, input().split())
    ndic = {}
    t = 0
    for i in range(K):
        t += 1
        co =list(map(int, input().split()))
        ndic[t]=co
    for j in range(M):
        nmap={}
        for key,value in ndic.items():
            # 방향이 위
            if value[3] == 1:
                # 원래 자리 0
                value[0] -= 1
                # 양 끝에 있으면 다음 이동방향 반대
                if value[0] ==0:
                    value[2]//=2
                    value[3] = 2
                if((value[0],value[1])) in nmap:
                    nmap[(value[0],value[1])].append(key)
                else:
                    nmap[(value[0], value[1])] = [key]
            # 방향이 아래
            elif value[3] == 2:
                # 원래 자리 0
                value[0] += 1
                # 양 끝에 있으면 다음 이동방향 반대
                if value[0] ==N-1:
                    value[2]//=2
                    value[3] = 1
                if((value[0],value[1])) in nmap:
                    nmap[(value[0],value[1])].append(key)
                else:
                    nmap[(value[0], value[1])] = [key]
            # 방향이 좌
            elif value[3] == 3:
                # 원래 자리 0
                value[1] -= 1
                # 양 끝에 있으면 다음 이동방향 반대
                if value[1] ==0:
                    value[2] //= 2
                    value[3] = 4
                if ((value[0], value[1])) in nmap:
                    nmap[(value[0], value[1])].append(key)
                else:
                    nmap[(value[0], value[1])] = [key]
            # 방향이 우
            elif value[3] == 4:
                # 원래 자리 0
                value[1] += 1
                # 양 끝에 있으면 다음 이동방향 반대
                if value[1] == N-1:
                    value[2] //= 2
                    value[3] = 3
                if ((value[0], value[1])) in nmap:
                    nmap[(value[0], value[1])].append(key)
                else:
                    nmap[(value[0], value[1])] = [key]
        dellist = []
        # print()
        # print(ndic)
        for key,value in nmap.items():
            if len(value)>1:
                # print(value)
                msiz=0
                for n in value:
                    if ndic[n][2]>msiz:
                        mkey=n
                        msiz=ndic[n][2]
                for l in value:
                    if l==mkey:
                        pass
                    else:
                        ndic[mkey][2]+=ndic[l][2]
                        dellist.append(l)
        # print(dellist)
        for d in dellist:
            del(ndic[d])

    ans = 0
    for key,value in ndic.items():
        # print(key,value)
        ans += value[2]
    print(f'#{tc+1} {ans}')