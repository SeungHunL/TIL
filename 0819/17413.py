A=input()
count=[0]*len(A)
ans=''
cnt=0
for i in range(len(A)):
    if A[i]=='<':
        count[i]=1
    elif A[i]=='>':
        count[i]=2
    elif A[i]==' ':
        count[i]=3
j=0
while 1:
    if A[i]=='<':
        s = i
    