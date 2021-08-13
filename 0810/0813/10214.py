R = int(input())
for _ in range(R):
    CS = SS = 0
    for i in range(9):
        C, S = map(int, input().split())
        CS += C
        SS += S
    if CS > SS:
        print('Yonsei')
    elif SS > CS:
        print('Korea')
    else:
        print('Draw')
