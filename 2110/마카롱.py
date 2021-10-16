from collections import deque

def solution(macaron):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def bfs(start, color):
        que = deque()
        que.append(start)
        ans = []
        while que:
            y, x = que.popleft()
            ans.append((y, x))
            for dx, dy in d:
                ty = y + dy
                tx = x + dx
                if 0 <= ty < 6 and 0 <= tx < 6:
                    if maps[ty][tx] == color and (ty,tx)not in ans:
                        que.append((ty, tx))
        if len(ans)>=3:
            for iy,ix in ans:
                maps[iy][ix]=0
                save[iy]-=1
            sa=[]
            for i in range(6):
                if save[i]:
                    for j in range(save[i]):
                        for k in range(6):
                            if maps[i][k]:
                                if k!=j:
                                    maps[i][k],maps[i][j]=maps[i][j],maps[i][k]
                                    sa.append((i,j))
                                break
            for ly,lx in sa:
                if maps[ly][lx]:
                    bfs((ly,lx),maps[ly][lx])


    maps = [[0] * 6 for q in range(6)]
    save = [0] * 6
    for i in macaron:
        x, c = i[0] - 1, i[1]
        maps[x][save[x]] = c
        save[x] += 1
        bfs((x,save[x]-1),c)
        print(save,'save')
        for k in maps:
            print(k)
        print()

    answer=[[0] * 6 for q in range(6)]
    for i in range(6):
        for j in range(6):
            answer[5-j][i]=f'{maps[i][j]}'
    for k in range(6):
        answer[k]=''.join(answer[k])
    print(answer)
    return answer
maca=[[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]
solution(maca)