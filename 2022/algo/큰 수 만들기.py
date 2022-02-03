def solution(number, k):
    answer = []
    for n in number:
        if answer and k:
            if answer[-1]>=n:
                answer.append(n)
            else:
                while answer and k and answer[-1]<n:
                    answer.pop()
                    k-=1
                answer.append(n)
        else:
            answer.append(n)

    return ''.join(answer)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
