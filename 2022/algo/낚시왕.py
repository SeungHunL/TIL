import sys
input=sys.stdin.readline
R,C,M = map(int, input().split())
answer=0
sharks=[]
point=[[0]*(C+1) for i in range(R+1)]
print(point)
for i in range(M):
    sharks.append(list(map(int, input().split())))
for j in range(1,C+1):
    catch=[]
    for s in range(len(sharks)):
        if sharks[s][1]==j:
            catch.append(s)
            answer+=sharks[s][4]
    while catch:
        sharks.pop(catch.pop())

    for idx in range(len(sharks)):
        s=sharks[idx]
        if s[3]==1:
            s[0]-=s[2]
            if s[0]<0:
                -1*s
        elif s[3]==2:
            s[0]+=s[2]
        elif s[3]==3:
            s[1] +=s[2]
        else:
            s[1] -=s[2]
        print(s)
        if point[s[0]][s[1]]:
            if sharks[point[s[0]][s[1]]][4]>s[4]:
                catch.append(idx)
            else:
                catch.append(point[s[0]][s[1]])
                point[s[0]][s[1]]=idx
        else:
            point[s[0]][s[1]]=idx
    while catch:
        sharks.pop(catch.pop())
print(answer)