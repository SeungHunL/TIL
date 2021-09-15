import sys

key = []
s = 0
for _ in range(9):
    n = int(sys.stdin.readline())
    key.append(n)
    s += n
flag=0
for i in range(9):
    for j in range(i+1, 9):
        if key[i] + key[j] == s - 100:
            key.pop(j)
            key.pop(i)
            flag=1
            break
    if flag:
        break
key.sort()
for __ in key:
    print(__)
