def lonely(lst):
    nlst = []
    nlst.append(lst[0])
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            nlst.append(lst[i])
    return nlst
print(lonely([1,1,3,3,0,1,1]))