from collections import deque

def solution(bridge_length, weight, truck_weights):
    move_on=deque()
    move_on_time=deque()
    wait=deque(truck_weights)
    time=1
    while wait or move_on:
        time+=1
        if wait and sum(move_on)+wait[0]<=weight:
            move_on.append(wait.popleft())
            move_on_time.append(bridge_length)
        move_on_time=deque(map((lambda x:x-1),move_on_time))
        if move_on and move_on_time[0]==0:
            move_on.popleft()
            move_on_time.popleft()
            
    return time

# print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))