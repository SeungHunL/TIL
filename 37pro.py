pib=int(input())
i=1
pibl=[]
pibl[0]=1
pibn=0
while i<=pib:
    pibl[i]=pibl[(i-1)]+i
    i+=1
print(pibl)
