h = input()


def score(i):
    if i[0] == 'A':
        s = 4
    elif i[0] == 'B':
        s = 3
    elif i[0] == 'C':
        s = 2
    elif i[0] == 'D':
        s = 1
    else:
        return '0.0'
    if i[1] == '+':
        return (s + 0.3)
    elif i[1] == '0':
        return (s + 0.0)
    else:
        return (s - 0.3)


print(score(h))
