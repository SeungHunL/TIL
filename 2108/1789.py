N = int(input())
i = 1
s = 0
while (1):
    s += i
    if s > N:
        print(i-1)
        break
    elif s==N:
        print(i)
        break
    i += 1