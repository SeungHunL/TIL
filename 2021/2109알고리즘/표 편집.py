def solution(n, k, cmd):
    exist = [1] * n
    ck = []

    while cmd:
        a = cmd.pop(0)

        if a[0] == 'D':
            i = 1
            while i <= int(a[2]):
                if exist[k + 1] == 1:
                    k += 1
                    i += 1
                else:
                    k += 1

        elif a[0] == 'U':
            i = 1
            while i <= int(a[2]):
                if exist[k - 1] == 1:
                    k -= 1
                    i += 1
                else:
                    k -= 1

        elif a[0] == 'C':
            ck.append(k)
            exist[k] = 0
            if k + 1 <= n - 1:
                k += 1
            else:
                k -= 1

        elif a[0] == 'Z':
            exist[ck.pop()] = 1

    answer = ''

    for l in exist:
        if l == 1:
            answer += 'O'
        else:
            answer += 'X'
    print(answer)
    return answer


solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
