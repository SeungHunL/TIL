import sys
stack =[]
for i in range(int(sys.stdin.readline())):
    N= int(sys.stdin.readline())
    if N:
        stack.append(N)
    elif stack:
        stack.pop()
ans=0
for j in stack:
    ans+=j
print(ans)