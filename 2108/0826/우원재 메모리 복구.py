for _ in range(int(input())):
    zo = input()
    if zo[-1] == '0':
        n = zo.count('10') * 2
    else:
        n = zo.count('10') * 2 + 1
    print(f'#{_ + 1} {n}')
    print(zo.count('10'))