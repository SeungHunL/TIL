import sys

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = [[tower[0],0]]
ans = [0]
for i in range(1,N):

    t = tower[i]
    if t > stack[0][0]:
        stack = [[t,i]]
        ans.append(0)
    elif t == stack[0][0]:
        stack = [[t,i]]
        ans.append(stack[0][0]+1)
    else:
        j = len(stack)-1
        while t >= stack[j][0]:
            stack.pop()
            stack.append([t,i])
            j -=1
        stack.append([t,i])
        ans.append(stack[j][1] + 1)

print(' '.join(map(str,ans)))