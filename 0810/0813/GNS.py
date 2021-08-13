def my_index(s):
    if s == "ZRO":
        return 0
    elif s == "ONE":
        return 1
    elif s == "TWO":
        return 2
    elif s == "THR":
        return 3
    elif s == "FOR":
        return 4
    elif s == "FIV":
        return 5
    elif s == "SIX":
        return 6
    elif s == "SVN":
        return 7
    elif s == "EGT":
        return 8
    elif s == "NIN":
        return 9

def my_value(ents):
    if ents == 0:
        return "ZRO"
    elif ents == 1:
        return "ONE"
    elif ents == 2:
        return "TWO"
    elif ents == 3:
        return "THR"
    elif ents == 4:
        return "FOR"
    elif ents == 5:
        return "FIV"
    elif ents == 6:
        return "SIX"
    elif ents == 7:
        return "SVN"
    elif ents == 8:
        return "EGT"
    elif ents == 9:
        return "NIN"


T = int(input())
for _ in range(T):
    N = [0] * 10
    L = ''
    A, B = input().split()
    tenet = list(input().split())
    for i in range(len(tenet)):
        N[my_index(tenet[i])] += 1
    for j in range(10):
        for k in range(N[j]):
            s = my_value(j)
            L += f'{s} '
    print(A)
    print(L)