# import sys
# sys.stdin = open("input.txt", "r")

def hex_to_bin(arr):
    h_list = ['A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    for text in arr:
        b = ''
        h = 0
        for t in range(6):
            if text == h_list[t]:
                h = 10 + t
                break
        if not h:
            h = int(text)
        while h > 0:
            b = str(h % 2) + b
            h //= 2
        while len(b) < 4:
            b = '0' + b
        result += b
    num_zero = 0
    for t in range(len(result)-1, -1, -1):
        if result[t] != '0':
            break
        num_zero += 1
    if num_zero:
        result = '0' * num_zero + result[:-num_zero]

    return result


def code_to_dec(arr, n):
    p_list = ['000' * n + '11' * n + '0' * n + '1' * n,
              '00' * n + '11' * n + '00' * n + '1' * n,
              '00' * n + '1' * n + '00' * n + '11' * n,
              '0' * n + '1111' * n + '0' * n + '1' * n,
              '0' * n + '1' * n + '000' * n + '11' * n,
              '0' * n + '11' * n + '000' * n + '1' * n,
              '0' * n + '1' * n + '0' * n + '1111' * n,
              '0' * n + '111' * n + '0' * n + '11' * n,
              '0' * n + '11' * n + '0' * n + '111' * n,
              '000' * n + '1' * n + '0' * n + '11' * n]
    dec = ''
    p = 0
    while p < 56 * n:
        temp = arr[p:p + (7 * n)]
        for t in range(10):
            if temp == p_list[t]:
                dec += str(t)
                break
        p += (7 * n)

    return dec


def is_corr(arr):
    o, e = 0, 0
    for t in range(len(arr)):
        if t % 2:
            e += int(arr[t])
        else:
            o += int(arr[t])
    if ((o * 3) + e) % 10:
        return

    return True


def my_sum(arr):
    sigma = 0
    for t in arr:
        sigma += int(t)

    return sigma


def code_split(arr):
    s_list = []
    if len(arr) % 56 == 0:
        return [arr]
    temp = ''
    for t in range(len(arr)-1, -1, -1):
        if arr[t] != '0':
            temp += arr[t]
        else:
            if not temp:
                continue
            if len(temp) % 56 == 0:
                s_list.append(temp[::-1])
                temp = ''
            else:
                temp += arr[t]

    return s_list


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    test_case = [input().strip() for _ in range(N)]

    mass = []
    for i in range(N):
        for j in range(M):
            if ord(test_case[i][j]) > 48:
                binary = hex_to_bin(test_case[i].strip('0'))
                for k in code_split(binary):
                    if k not in mass:
                        mass.append(k)
                break

    ans = 0
    for t_case in mass:
        length = len(t_case) // 56
        conv_code = code_to_dec(t_case, length)
        print(conv_code)
        if is_corr(conv_code):
            ans += my_sum(conv_code)

    print('#{} {}'.format(tc, ans))