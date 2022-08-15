def never(qu):
    a=qu.pop(1)
    qu.sort()
    return [a]+qu
queue=[0,10,100]
print(never(queue))