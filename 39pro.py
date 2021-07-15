a=[2,4,6,8,10]
p=10
q=5
count1=0
for i in range(0,len(a)-1):
    if p==a[i]:
        print(f'{p} => True')
        break
    else:
        print(f'{p} => False')
    if q==a[i]:
        print(f'{q} => True')
    else:
        print(f'{q} => False')
