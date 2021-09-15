import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    call = []
    ans = 0
    count = 0
    for i in range(N):
        call.append(sys.stdin.readline().strip())
        for k in range(len(call)-1):
            if len(call[i]) >= len(call[k]):
                for m in range(len(call[k])):
                    if call[k][m] != call[i][m]:
                        break
                else:
                    ans=1
    if ans:
        print('NO')
    else:
        print('YES')