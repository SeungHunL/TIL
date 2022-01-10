from collections import deque

def solution(priorities, location):
    target = priorities[location]
    
    new_priorities = deque()

    dec_location=0
    for idx,priority in enumerate(priorities):
        if priority >= target:
            new_priorities.append(priority)
        else:
            if idx<location:
                dec_location+=1
    location-=dec_location

    time=0
    while new_priorities:
        cur=new_priorities[0]
        cur_idx=0
        for idx,priority in enumerate(new_priorities):
            if cur < priority:
                cur = priority
                cur_idx = idx
        
        new_priorities=list(new_priorities)
        new_priorities=deque(new_priorities[cur_idx:] + new_priorities[:cur_idx])
        if cur_idx<=location:
            location-=cur_idx
        else:
            location=len(new_priorities)+location-cur_idx
            
        time+=1
        if location==0:
            return time
        else:
            new_priorities.popleft()
            location-=1