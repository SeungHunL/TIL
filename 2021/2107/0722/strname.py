def get_strong_word(*args):
    sum1 = 0
    for i in range(len(args[0])):
        sum1 += ord(args[0][i])
    sum2 = 0
    for i in range(len(args[1])):
        sum2 += ord(args[1][i])
    if sum1 > sum2:
        return args[0]
    else:
        return args[1]
print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))    