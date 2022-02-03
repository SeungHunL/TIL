def solution(n, times):
    end=n*max(times)
    start=0
    while end>=start:
        mid = (end + start) // 2
        print(start,end)
        num = sum(map(lambda x:mid//x,times))
        if num>=n:
            answer=mid
            end = mid - 1
        elif num<n:
            start=mid+1
    return answer
print(solution(6,[7, 10]))