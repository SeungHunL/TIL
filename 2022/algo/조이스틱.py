def flow(arr):
    cnt=0
    mcnt=0
    midx=0
    for i in range(len(arr)):
        if arr[i]:
            cnt+=1
        else:
            if mcnt < cnt:
                mcnt=cnt
                midx=i
            cnt=0
    # print(midx-mcnt-1,len(arr)-midx)
    # print(len(arr)-1,midx-mcnt-1+len(arr)-midx+min(abs(midx-mcnt-1),len(arr)-midx))
    if mcnt:
        return min(len(arr)-1,midx-mcnt-1+len(arr)-midx+min(abs(midx-mcnt-1),len(arr)-midx))
    else:
        return len(arr)-1
def solution(name):
    answer = 0
    order=[]
    for i in name:
        answer+=min(ord(i)-65,91-ord(i))
        if i=='A':
            order.append(0)
        else:
            order.append(1)
    return answer + flow(order)

print(solution("JAN"))
print(solution("JEROEN"))
print(solution("ZZAAAAAAAAAAZ"))