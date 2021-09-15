def solution(numbers):
    answer = []
    for i in numbers:
        n = i
        i = bin(i)[2:]
        while 1:
            n += 1
            bin_n = bin(n)[2:]
            k = len(bin_n) - len(i)
            cnt = 0
            if k:
                n = int('10' + '1' * (len(i) - 1), 2)
                answer.append(n)
                break

            else:
                for idx in range(len(i)):
                    if cnt > 2:
                        break
                    elif i[-idx] != bin_n[-idx]:
                        cnt += 1

                if cnt <= 2:
                    answer.append(n)
                    break
    print(answer)
    return answer


solution([2, 7])
