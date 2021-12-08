T = int(input())

token = {
    '0b0001101': 0,
    '0b0011001': 1,
    '0b0010011': 2,
    '0b0111101': 3,
    '0b0100011': 4,
    '0b0110001': 5,
    '0b0101111': 6,
    '0b0111011': 7,
    '0b0110111': 8,
    '0b0001011': 9,
}


for _ in range(T):
    N, M = map(int, input().split())
    string = []
    ans = 0
    flag=0
    for n in range(N):
        string = input()
        if ans and flag==0:
            continue

        for i in range(M - 56):
            if string[-i - 1] == '1':
                end = M - i
                break
        else:
            continue

        t=[]
        for j in range(8):
            teststr = '0b'+string[end - 7 * (7 - j) - 7:end - 7 * (7 - j)]
            a=token[teststr]
            t.append(a)
            ans += a

        snum = (t[0] + t[2] + t[4] + t[6]) * 3 + t[1] + t[3] + t[5]
        scode = 10 - snum % 10 if snum%10 else 0
        if scode != t[-1]:
            flag=1
    if flag:
        print(f'#{_ + 1} 0')
    else:
        print(f'#{_ + 1} {ans}')
