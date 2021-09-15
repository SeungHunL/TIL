for _ in range(int(input())):
    s, r = map(str,input().split())
    one = ['A', 'D', 'O', 'P', 'Q', 'R']
    zer = ['C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if len(s) != len(r):
        print(f'#{_ + 1} DIFF')
        continue
    for i in range(len(s)):
        if s[i] in zer and r[i] in zer:
            continue
        elif s[i] in one and r[i] in one:
            continue
        elif s[i] == 'B' and r[i] == 'B':
            continue
        else:
            print(f'#{_ + 1} DIFF')
            break
    else:
        print(f'#{_ + 1} SAME')
