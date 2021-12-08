def comb(n,r):
    if not r:
        calsum(t)
    elif n<r:
        return
    else:
        t[r-1]=n-1
        comb(n-1,r-1)
        comb(n-1,r)

def calsum(l):
    a=l[0]
    b=l[1]
    c=l[2]
    asum = float(f'{(score[a][b]*score[b][c]*score[c][a]):.2f}')
    acost = cost[a]+cost[b]+cost[c]
    ans=[a,b,c,asum,acost]
    board.append(ans)

for _ in range(int(input())):
    N, M, K = map(int, input().split())
    score = [[0] * N for __ in range(N)]
    for m in range(M):
        a, b, c = map(float, input().split())
        score[int(a)-1][int(b)-1] = c
        score[int(b) - 1][int(a) - 1] = c
    cost = list(map(int, input().split()))
    limit = list(map(int, input().split()))

    t=[0]*3
    board=[]
    comb(N,3)
    print(board)
    lenboard=len(board)
    for i in range(lenboard):
        if board[i][4]<=limit[2]:
            print("#############################################################")
            print(i)
            for j in range(lenboard):
                if board[j][4] <= limit[1]:
                    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print(j)
                    for l in range(lenboard):
                        if board[l][4] <= limit[0]:
                            used=[0]*5
                            # i j l 선정
                            for a in [i,j,l]:
                                used[board[a][0]]+=1
                                used[board[a][1]] += 1
                                used[board[a][2]] += 1
                            for k in range(5):
                                if used[k]>2:
                                    break
                            else:
                                print(i,j,l)
                                totalpop=f'{board[i][3]+board[j][3]+board[l][3]:.2f}'
                                print(totalpop)