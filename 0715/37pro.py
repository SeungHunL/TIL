pib=int(input())
i=1
pibl=[]
pibl=[0]*pib
pibl[0]=1
pibl[1]=1
pibn=0
while i<=(pib-2):
    pibl[i+1]=pibl[i]+pibl[i-1]
    i+=1
print(pibl)
