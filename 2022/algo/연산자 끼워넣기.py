import sys


def selectops():
    global max_result, min_result
    if len(ops) == N:
        ans = A[0]
        for i in range(1, N):
            if ops[i] == 0:
                ans += A[i]
            elif ops[i] == 1:
                ans -= A[i]
            elif ops[i] == 2:
                ans *= A[i]
            else:
                if ans < 0 and A[i] > 0:
                    ans //= -A[i]
                    ans *= -1
                else:
                    ans //= A[i]

        if ans > max_result:
            max_result = ans
        if ans < min_result:
            min_result = ans
    else:
        for x in range(4):
            if Operator[x]:
                ops.append(x)
                Operator[x] -= 1
                selectops()
                ops.pop()
                Operator[x] += 1


input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Operator = list(map(int, input().split()))
ops = [0]
max_result = -1e9
min_result = 1e9
selectops()
print(max_result)
print(min_result)
