import sys
input=sys.stdin.readline

card=[]
t=int(input().strip())
for q in range(t):
    card.append(int(input().strip()))
card.sort()

ans=0
if t>1:
    while len(card)>2:
        r=card[0]+card[1]
        card=[card[0]+card[1]]+card[2:]
        card.sort()
        ans+=r
    else:
        ans+=card[0]+card[1]
print(ans)