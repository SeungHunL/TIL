def test(b):
    count = []
    for i in range(len(b)):
        if b[i] in ('(', ')', '{', '}'):
            if b[i] == '{':
                count.append('{')
            elif b[i] == '(':
                count.append('(')
            elif len(count) != 0 and b[i] == '}' and count[-1] == '{':
                count.pop()
            elif len(count) != 0 and b[i] == ')' and count[-1] == '(':
                count.pop()
            else:
                return 0
    else:
        if count:
            return 0
        else:
            return 1


for _ in range(int(input())):
    L = input()
    print(f'#{_ + 1} {test(L)}')
