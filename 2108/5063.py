T = int(input())
for num in range(T):
    r, e, c = map(int, input().split())
    if r < e - c:
        print('advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('do not advertise')
