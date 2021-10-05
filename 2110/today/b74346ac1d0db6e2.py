# import sys
#
# sys.stdin = open("input.txt", "r")

sixteen = '0123456789ABCDEF'


def comp(n, num16):
    num2 = ''
    for i in range(n - 1, -1, -1):
        now = num16[i]
        for j, val in enumerate(sixteen):
            if now == val:
                # 2진수로 만들기
                temp = ''
                while j:
                    temp = str(j % 2) + temp
                    j = j // 2
                if len(temp) < 4:
                    temp = '0' * (4 - len(temp)) + temp

                num2 = temp + num2
                break

    return num2


key = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}


def is_10(pwcode):
    result = 0

    for r in range(0, 8, 2):
        result += int(pwcode[r]) * 3

    for r in range(1, 8, 2):
        result += int(pwcode[r])

    if result % 10:
        return False
    return True


for tc in range(int(input())):
    n, m = map(int, input().strip().split())
    pwlist = set()
    for i in range(n):
        temp = input().strip().rstrip('0')

        check = ''
        flag = 0
        while j > -1:
            if temp[j] != '0':
                flag = 1
                check = temp[j] + check
                j -= 1
            else:
                if flag:
                    pwlist.add(check)
                    check = ''
                    flag = 0
                j -= 1
    # 맨 앞자리까지 연결될 때
    if flag and check:
        pwlist.add(check)

    anslst = []

    for code in pwlist:
        # 2진수로 만들기
        num2 = comp(len(code), code)
        num2 = num2.rstrip('0')
        # 길이가 56의 배수가 되도록 만들기
        if len(num2) % 56 != 0:
            num2 = '0' * (56 - len(num2) % 56) + num2
        # 56의 몇 배인지
        multiple = len(num2) // 56
        for mtp in range(1, multiple + 1):
            jump = 7 * mtp
            start = jump
            pwcode = ''
            while start <= len(num2):
                c = num2[start - jump:start]
                if c[-1] == '0':
                    start += jump
                    continue
                else:
                    k = ''
                    for idx in range(0, jump, mtp):
                        k += c[idx]
                    pw = key.get(k)
                    if pw == None:
                        break
                    else:
                        pwcode += pw
                    start += jump
            print(pwlist)
            if len(pwcode) == 8:
                if is_10(pwcode):
                    anslst.append(pwcode)
    ans = 0
    if anslst:
        for a in anslst:
            ans += sum(list(map(int, list(a))))
    print(f'#{tc + 1} {ans}')
