import sys

model = []
stack = []
test = []
ans =[]
N = int(sys.stdin.readline())
for i in range(N):
    model.append(int(sys.stdin.readline()))
k = 0
for j in range(1, N + 1):
    test.append(j)
    ans.append('+')

    while test and test[-1] == model[k]:
        stack.append(test.pop())
        k += 1
        ans.append('-')
if test:
    print('NO')
else:
    for l in range(len(ans)):
        print(ans[l])