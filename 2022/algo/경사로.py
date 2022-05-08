import sys

input = sys.stdin.readline

N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def load(arr):
    global ans
    for i in range(len(arr)):
        line = arr[i]
        check = [0] * len(line)
        flag = False
        j = 0
        while not flag:
            if j >= N - 1:
                ans += 1
                break
            if line[j] == line[j + 1]:
                j += 1

            elif line[j] == line[j + 1] + 1 and check[j+1]==0:
                if j + L >= N:
                    break
                j += 1
                check[j]=1
                a = line[j]
                for k in range(1, L):
                    if line[j + k] != a or check[j + k]:
                        flag = True
                        break
                    check[j + k] = 1
                else:
                    j += L - 1

            elif line[j] == line[j + 1] - 1 and check[j]==0:

                if j < L-1:
                    break
                check[j]=1
                j += 1
                a = line[j - 1]
                for k in range(1, L):
                    if line[j - 1 - k] != a or check[j - 1 - k]:
                        flag = True
                        break
                    check[j - 1 - k] = 1
            else:
                break


load(maps)
load(list(map(list, zip(*maps))))
print(ans)
