for _ in range(int(input())):
    L = list(input())
    while 1:
        for i in range(1,len(L)):
            if L[i-1]==L[i]:
                L.pop(i-1)
                L.pop(i-1)
                break
        else:
            break
    print(f'#{_+1} {len(L)}')

