L=int(input())
model=input()
N=int(input())
test=[0]*N
ans = []

for _ in range(N):
    test[_]=input()
for __ in range(N):
    sample = f'{test[__]} {test[__]}'
    sample2 = ''
    for i in range(len(sample)):
        if sample[i]=='3':
            sample2 += f'{1}'
        elif sample[i]=='1':
            sample2 += f'{3}'
        elif sample[i]=='2':
            sample2 += f'{4}'
        elif sample[i]=='4':
            sample2 += f'{2}'
        else:
            sample2 += ' '
    sample2 = sample2[::-1]
    if (model in sample) or (model in sample2):
        ans.append(test[__])
print(len(ans))
for ___ in ans:
    print(___)