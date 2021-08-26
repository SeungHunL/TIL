T= int(input())
N=list(map(int,input().split()))
c=d=0
for i in range(T):
    c += (N[i]//30+1)*10
    d += (N[i]//60+1)*15
if c>d:
    print(f'M {d}')
elif c==d:
    print(f'Y M {c}')
else:
    print(f'Y {c}')