import sys

def nqueen(n,board,visit,last):
    global ans
    # print(n,board,visit,last)
    if n==L:
        c=board.count('a')+board.count('e')+board.count('i')+board.count('o')+board.count('u')
        if c>0 and n-c>1:
            print(''.join(board))
            ans+=1
        return
    if last==C:
        return
    for i in range(last,C):
        if visit[i]==0:
            visit[i]=1
            nqueen(n+1,board+[ts[i]],visit,i+1)
            visit[i] = 0


input = sys.stdin.readline
L,C = map(int,input().split())
ts=list(input().split())
ts.sort()
ans=0
nqueen(0,[],[0]*C,0)

