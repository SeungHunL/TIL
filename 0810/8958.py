T = int(input())
for num in range(T):
    case = input()
    t = score = 0
    for i in case:
        if i == 'O':
            t += 1
        else:
            t = 0
        score += t
    print(score)
