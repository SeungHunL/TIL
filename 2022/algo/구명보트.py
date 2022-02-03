def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    pd={}
    np=[]
    for i in people:
        if i in pd:
            pd[i]+=1
        else:
            np.append(i)
            pd[i]=1
    print(np)
    # people=list(pd.keys())
    while people:
        answer += 1
        s=people[0]
        w = limit - s
        pd[s]-=1
        if pd[s] == 0:
            people.remove(s)
        if w >=40:
            for i in people:
                if i <= w:
                    pd[i]-=1
                    if pd[i] == 0:
                        people.remove(i)
                    break

    return answer

print(solution([70, 50, 80, 50],100))