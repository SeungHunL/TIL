import heapq
def solution(jobs):
    # heap=sorted(jobs)
    heap=[]
    for job in jobs:
        heapq.heappush(heap,job)

    time=0
    possible=[]
    answer=[]
    while heap or possible:
        while heap and heap[0][0]<=time:
            print(heap)
            item=heapq.heappop(heap)
            heapq.heappush(possible,item)

        if possible:
            todo_heap = []
            for item in possible:
                heapq.heappush(todo_heap,(item[1]+time-item[0],item))
            todo=heapq.heappop(todo_heap)[1]
            possible.remove(todo)

        else:
            todo=heapq.heappop(heap)
            time =todo[0]
        answer.append(todo[1] + time - todo[0])
        time += todo[1]
    # print(time)
    print(answer)
    return (sum(answer))//len(answer)
print(solution([[0, 3], [1, 9], [2, 6],[1,3],[1,1],[1,4]]))
print(solution([[0, 3], [1, 3], [2, 6],[1,9]]))