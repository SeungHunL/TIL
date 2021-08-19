N = list(map(int,input()))
count = [0] * 10
cnt = 0
for i in range(len(N)):
    if count[N[i]]>0:
        count[N[i]] -= 1
    elif count[6] > 0 and N[i] == 9:
        count[6]-=1
    elif count[9] > 0 and N[i] == 6:
        count[9]-=1
    else:
        cnt += 1
        for k in range(10):
            count[k] += 1
        count[N[i]] -= 1
print(cnt)
