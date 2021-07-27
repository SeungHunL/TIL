Tcase = int(input())
for i in range(Tcase):
    s = input()
    for j in (0,len(s)+1):
        if j == 0:
            result = s[j]
        elif s[j] == '@':
            result *= 3
        elif s[j] == '%':
            result += 5
        elif s[j] == '#':
            result -= 7
print(result)