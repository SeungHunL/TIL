T = int(input())
AXIS = Q1 = Q2 = Q3 = Q4 = 0
for num in range(T):
    A, B = map(int, input().split())
    if (A and B) == 0:
        AXIS += 1
    elif A > 0 and B > 0:
        Q1 += 1
    elif A < 0 and B < 0:
        Q3 += 1
    elif B < 0:
        Q4 += 1
    else:
        Q2 += 1
print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')
