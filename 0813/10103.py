R = int(input())
CS = SS = 100
for _ in range(R):

    C, S = map(int, input().split())
    if C > S:
        SS -= C
    elif S > C:
        CS -= S
print(CS)
print(SS)