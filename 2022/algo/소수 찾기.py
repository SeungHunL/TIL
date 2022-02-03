def dfs(arr, visit,numb,answer):
    if len(numb) == len(arr):
        N=int(''.join(numb))
        if N not in answer:
            for i in range(2, N // 2):
                if not N % i:
                    break
            else:
                answer.append(N)
    else:
        for i in range(len(arr)):
            if visit[i]:
                pass
            else:
                visit[i] = 1
                numb.append(arr[i])
                dfs(arr, visit, numb,answer)
                numb.pop()
                visit[i] = 0


def solution(numbers):
    answer = set()
    numbers = list(numbers)
    check = [0] * len(numbers)
    numb = []
    answer=[]
    dfs(numbers, check,numb,answer)

    return len(answer)

print(solution("011"))