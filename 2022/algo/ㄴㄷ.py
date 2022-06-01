import random
dss=[]
for i in range(10000):
    x= random.randrange(1,100)
    y= random.randrange(1,100)
    dss.append((x,y))
for i in dss:
    print(i)