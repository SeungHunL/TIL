from collections import deque
def solution(n, edge):
    dic={}
    for route in edge:
        if route[0] in dic:
            dic[route[0]].append(route[1])
        else:
            dic[route[0]]=[route[1]]
        if route[1] in dic:
            dic[route[1]].append(route[0])
        else:
            dic[route[1]]=[route[0]]
    queue=deque([1])
    nq=[]
    used = [0]*(n+1)
    while queue:
        t=queue.popleft()
        used[t]=1
        for i in dic[t]:
            if not used[i]:
                nq.append(i)
        if not queue:
            if not nq:
                return answer
            queue=deque(nq)
            answer=len(nq)
            nq=[]
    return answer
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])